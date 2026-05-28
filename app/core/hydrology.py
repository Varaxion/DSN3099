import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from imblearn.over_sampling import SMOTE
from sklearn.utils import shuffle
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

warnings.filterwarnings("ignore")

# Paths
CORE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CORE_DIR)

# -----------------------------
# 1. ARIMA Timeseries Forecaster Logic
# -----------------------------
def _arima_forecast(filename, target_column, freq, steps):
    data_path = os.path.join(BASE_DIR, 'data', f'{filename.capitalize()}.xlsx')
    raw_data_df = pd.read_excel(data_path, header=0)
    raw_data_df['Date'] = pd.to_datetime(raw_data_df['Date'])

    for col in raw_data_df.columns[1:]:
        raw_data_df[col] = raw_data_df[col].fillna(raw_data_df[col].mean())

    data = pd.DataFrame({'Date': raw_data_df['Date'], target_column: raw_data_df[target_column]})
    data = data.set_index(['Date'])
    
    resampled = data.resample(freq).sum()

    values = resampled[target_column].values.reshape(-1, 1).astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    
    scale_df = resampled.copy()
    scale_df[target_column] = scaled
    scale_df.reset_index(inplace=True)
    scale_df = scale_df.rename(columns={'Date': 'ds', target_column: 'y'})

    model = sm.tsa.ARIMA(scale_df['y'], order=(5,1,0))
    arima_model = model.fit()

    forecast = arima_model.forecast(steps=steps)
    forecast_dates = pd.date_range(start=scale_df['ds'].iloc[-1], periods=steps, freq=freq)
    
    df4 = pd.DataFrame({'Date': forecast_dates, target_column: forecast})
    
    val = scaler.inverse_transform(df4[target_column].values.reshape(-1, 1).astype('float32'))
    df4[target_column] = abs(val)

    # Save output
    safe_target = target_column.replace(' ', '_').lower()
    forecast_dir = os.path.join(BASE_DIR, 'data', 'forecast')
    os.makedirs(forecast_dir, exist_ok=True)
    out_path = os.path.join(forecast_dir, f'{filename.lower()}_{safe_target}_forecast.csv')
    df4.to_csv(out_path, index=False)

    return df4

def discharge_forecast(filename, wtd):
    steps = 30 * 25 if wtd == 0 else 3000
    return _arima_forecast(filename, 'Discharge', 'D', steps)

def flood_runoff_forecast(filename, wtd):
    steps = 30 * 25 if wtd == 0 else 3000
    return _arima_forecast(filename, 'flood runoff', 'D', steps)

def daily_runoff_forecast(filename, wtd):
    steps = 30 * 25 if wtd == 0 else 3000
    return _arima_forecast(filename, 'daily runoff', 'D', steps)

def weekly_runoff_forecast(filename, wtd):
    steps = 25 if wtd == 0 else 450
    return _arima_forecast(filename, 'weekly runoff', 'W-SUN', steps)


# -----------------------------
# 2. LDA Classification Logic
# -----------------------------
def flood_classifier(filename, fd):
    data_path = os.path.join(BASE_DIR, 'data', f'{filename.capitalize()}.xlsx')
    data1 = pd.read_excel(data_path)

    for i in range(1, len(data1.columns)):
        data1[data1.columns[i]] = data1[data1.columns[i]].fillna(data1[data1.columns[i]].mean())

    y = data1['Flood']

    for i in range(len(y)):
        if y[i] >= 0.1:
            y[i] = 1

    y = pd.DataFrame(y)
    data1.drop('Flood', axis=1, inplace=True)

    d1 = pd.DataFrame()
    d1["Day"] = data1['Date']
    d1['Months'] = data1['Date']
    d1['Year'] = data1['Date']
    data1['Date'] = pd.to_datetime(data1['Date'])
    d1["Year"] = data1.Date.dt.year
    d1["Months"] = data1.Date.dt.month
    d1["Day"] = data1.Date.dt.day

    data1.drop('Date', inplace=True, axis=1)

    values = data1.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    data1 = pd.DataFrame(scaled, columns=data1.columns)

    data1 = pd.concat([d1, data1], axis=1)

    locate = 0
    for i in range(len(data1["Day"])):
        if data1["Day"][i] == 31 and data1["Months"][i] == 12 and data1["Year"][i] == 2015:
            locate = i
            break

    i = locate + 1

    x_train = data1.iloc[0:i, :]
    y_train = y.iloc[0:i]
    x_test = data1.iloc[i:, :]
    y_test = y.iloc[i:]

    x_train.drop(labels=['Day', 'Months', 'Year'], inplace=True, axis=1)
    x_test.drop(labels=['Day', 'Months', 'Year'], inplace=True, axis=1)

    sm_sampler = SMOTE(random_state=2)
    X_train_res, Y_train_res = sm_sampler.fit_resample(x_train, y_train)

    x_train, y_train = shuffle(X_train_res, Y_train_res, random_state=0)

    clf1 = LinearDiscriminantAnalysis()
    clf1.fit(x_train, y_train)

    y_predict3 = clf1.predict(x_test)
    mae = mean_absolute_error(y_test, y_predict3)

    xx = np.array(fd).reshape((-1, 4))
    xx = clf1.predict(xx)
    return xx, mae


# -----------------------------
# 3. Dynamic Chart Plotter
# -----------------------------
def plot_flood_graph(filename, data, selected_idx, is_future=False):
    # Get window of 15 days before and 15 days after
    start_idx = max(0, selected_idx - 15)
    end_idx = min(len(data) - 1, selected_idx + 15)
    
    window_data = data.iloc[start_idx:end_idx + 1]
    dates = pd.to_datetime(window_data['Date'])
    
    y_values = window_data['Discharge']
    
    selected_date = pd.to_datetime(data['Date'].iloc[selected_idx])
    selected_val = data['Discharge'].iloc[selected_idx]
    
    fig = plt.figure(figsize=(12, 7))
    fig.suptitle(f"Discharge Trend - {filename.capitalize()}", fontsize=18, color='#f1f5f9', fontweight='bold', y=0.96)
    
    ax = fig.add_subplot(111)
    
    line_color = '#3b82f6' if not is_future else '#a78bfa'
    label_text = 'Historical Discharge' if not is_future else 'Forecasted Discharge'
    
    ax.plot(dates, y_values, color=line_color, linewidth=2.5, label=label_text)
    
    # Highlight the selected date
    ax.axvline(x=selected_date, color='#ef4444', linestyle='--', alpha=0.8, linewidth=1.5, label='Selected Date')
    ax.scatter(selected_date, selected_val, color='#ef4444', s=100, zorder=5, edgecolor='#f1f5f9', linewidth=1.5)
    
    # Add value annotation
    ax.annotate(f"{selected_val:.2f}", 
                xy=(selected_date, selected_val), 
                xytext=(10, 10), 
                textcoords='offset points', 
                color='#ef4444', 
                fontweight='bold',
                fontsize=12,
                bbox=dict(boxstyle="round,pad=0.3", fc="#0d1424", ec="#ef4444", lw=1, alpha=0.8))

    ax.set_ylabel("Discharge (m³/s)", fontsize=14, color='#f1f5f9', fontweight='bold', labelpad=15)
    ax.set_xlabel("Date", fontsize=14, color='#f1f5f9', fontweight='bold', labelpad=15)
    
    leg = ax.legend(fontsize=13, facecolor='#0d1424', edgecolor='none')
    for text in leg.get_texts():
        text.set_color('#f1f5f9')

    ax.set_facecolor('#0d1424')
    fig.patch.set_facecolor('#0a0e1a')
    ax.tick_params(colors='#f1f5f9', labelsize=11)
    ax.grid(True, linestyle='--', alpha=0.15, color='#94a3b8')
    
    fig.autofmt_xdate()

    img_path = os.path.join(BASE_DIR, 'static', 'img', 'flood.png')
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    
    plt.savefig(img_path, facecolor=fig.get_facecolor(), bbox_inches='tight', dpi=120)
    plt.close(fig)


# -----------------------------
# 4. Master Hydrology Core Driver
# -----------------------------
def drive(filename, userDate):
    try:
        filename = filename.lower()
        data_path = os.path.join(BASE_DIR, 'data', f'{filename.capitalize()}.xlsx')
        data = pd.read_excel(data_path)

        userDate = pd.to_datetime(userDate)
        lastDate = pd.to_datetime(data['Date'].iloc[-1])
        
        is_future = userDate > lastDate

        if not is_future:
            for col in data.columns[1:]:
                data[col] = data[col].fillna(data[col].mean())

            data['Date'] = pd.to_datetime(data['Date'])

            def existingPrediction(i):
                fd = data.iloc[i, 1:5].tolist()
                result, mae = flood_classifier(filename, fd)

                return {
                    'discharge': round(data.iloc[i, 1], 2),
                    'floodRunoff': round(data.iloc[i, 2], 2),
                    'dailyRunoff': round(data.iloc[i, 3], 2),
                    'weeklyRunoff': round(data.iloc[i, 4], 2),
                    'meanAbsoluteError': round(mae, 2),
                    'predicted': 'Normal' if result == 0 else 'High',
                    'actualFlood': 'Normal' if data.iloc[i, -1] == 0 else 'High'
                }

            for i in range(len(data)):
                if data['Date'].iloc[i].date() == userDate.date():
                    plot_flood_graph(filename, data, i, is_future=False)
                    return existingPrediction(i)

            return None

        else:
            wtd = 1
            d1 = discharge_forecast(filename, wtd)
            d2 = flood_runoff_forecast(filename, wtd)
            d3 = daily_runoff_forecast(filename, wtd)
            d4 = weekly_runoff_forecast(filename, wtd)

            expanded_weekly = np.repeat(d4['weekly runoff'].values, 7)
            if len(expanded_weekly) < len(d1):
                expanded_weekly = np.pad(expanded_weekly, (0, len(d1) - len(expanded_weekly)), 'edge')
            expanded_weekly = expanded_weekly[:len(d1)]

            data1 = pd.concat([d1, d2['flood runoff'], d3['daily runoff']], axis=1)
            data1['weekly runoff'] = expanded_weekly
            data1['Date'] = pd.to_datetime(data1['Date'])

            def futurePrediction(i):
                fd = data1.iloc[i, 1:].tolist()
                result, mae = flood_classifier(filename, fd)

                return {
                    'discharge': round(data1['Discharge'].iloc[i], 2),
                    'floodRunoff': round(data1['flood runoff'].iloc[i], 2),
                    'dailyRunoff': round(data1['daily runoff'].iloc[i], 2),
                    'weeklyRunoff': round(data1['weekly runoff'].iloc[i], 2),
                    'meanAbsoluteError': 'NIL',
                    'predicted': 'Normal' if result == 0 else 'High',
                    'actualFlood': 'NIL'
                }

            for i in range(len(data1)):
                if data1['Date'].iloc[i].date() == userDate.date():
                    plot_flood_graph(filename, data1, i, is_future=True)
                    return futurePrediction(i)

            return None

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"An error occurred in hydrology.drive(): {e}")
        return None
