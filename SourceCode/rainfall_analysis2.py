import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, explained_variance_score


def predict_rainfall(year, region):
    data = pd.read_csv(r'SourceCode\rainfall_data\Sub_Division_IMD_2021.csv')

    if data.isna().sum().sum() > 0:
        # Remove rows containing NaN values
        data.dropna(inplace=True)

    data_numeric = data.select_dtypes(include=[np.number])  # Select only numeric columns
    data_filled = data_numeric.fillna(data_numeric.mean())  # Fill missing values with mean

    # Function to plot the graphs
    def plot_graphs(groundtruth, prediction, title):
        N = 9
        ind = np.arange(N)  # the x locations for the groups
        width = 0.27  # the width of the bars

        fig = plt.figure(figsize=(18, 10))
        fig.suptitle(title, fontsize=12)
        ax = fig.add_subplot(111)
        rects1 = ax.bar(ind, groundtruth, width, color='m')
        rects2 = ax.bar(ind + width, prediction, width, color='c')

        ax.set_ylabel("Amount of rainfall")
        ax.set_xticks(ind + width)
        ax.set_xticklabels(('APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'))
        ax.legend((rects1[0], rects2[0]), ('Ground truth', 'Prediction'))

        for rect in rects1:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h), ha='center', va='bottom')
        for rect in rects2:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h), ha='center', va='bottom')

        plt.savefig(r'SourceCode\static\rainfall_image\rainfall.png')

    def data_generation(year, region):
        temp = data[['SUBDIVISION', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                     'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[data['YEAR'] == year]
        data_year = np.asarray(temp[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                                      'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[temp['SUBDIVISION'] == region])
        X_year = None
        y_year = None
        for i in range(data_year.shape[1] - 3):
            if X_year is None:
                X_year = data_year[:, i:i + 3]
                y_year = data_year[:, i + 3]
            else:
                X_year = np.concatenate((X_year, data_year[:, i:i + 3]), axis=0)
                y_year = np.concatenate((y_year, data_year[:, i + 3]), axis=0)

        return X_year, y_year

    def data_generation2(region):
        region_data = np.asarray(data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                                       'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[data['SUBDIVISION'] == region])

        X = None
        y = None
        for i in range(region_data.shape[1] - 3):
            if X is None:
                X = region_data[:, i:i + 3]
                y = region_data[:, i + 3]
            else:
                X = np.concatenate((X, region_data[:, i:i + 3]), axis=0)
                y = np.concatenate((y, region_data[:, i + 3]), axis=0)

        return X, y

    def prediction2(year, region):
        # Generate test data
        X_testing, Y_testing = data_generation(year, region)

        # Generate training data
        X_train, y_train = data_generation2(region)

        # Train Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_testing)
        mae = mean_absolute_error(Y_testing, y_pred)
        score = explained_variance_score(Y_testing, y_pred)

        # Plot and save the graph
        plot_graphs(Y_testing, y_pred, "Year: " + str(year) + '  Region: ' + str(region))
        return mae, score

    print("############", year, type(int(year)), region, type(region),
          "77777777777777777777777777&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    mae, score = prediction2(int(year), region)
    mae = format(round(float(mae), 2))
    score = format(round(float(score), 2))
    return mae, score
