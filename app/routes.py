import os
import unicodedata
import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.core.hydrology import drive as flood_predict
from app.core.rainfall import predict_rainfall

main_bp = Blueprint('main', __name__)

CORE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = CORE_DIR  # package directory /app

# -----------------------------
# Blood Bank Search Logic Setup
# -----------------------------
def norm(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    s = unicodedata.normalize("NFKD", s)
    return s.lower()

def load_blood_banks():
    try:
        csv_path = os.path.join(BASE_DIR, 'data', 'healthcare', 'blood-banks-india.csv')
        if not os.path.exists(csv_path):
            print(f"[ERROR] Blood banks dataset not found at {csv_path}")
            return pd.DataFrame()
        df = pd.read_csv(csv_path, dtype=str, encoding="utf-8").fillna("")
        df.columns = df.columns.str.strip().str.lower()
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip()  # Fix: State and City names remain in original Title Case!
        contact_cols = [c for c in df.columns if "contact" in c or "phone" in c or "mobile" in c]
        if contact_cols:
            df.rename(columns={contact_cols[0]: "contact"}, inplace=True)
        print("[SUCCESS] Loaded Blood Bank database successfully.")
        return df
    except Exception as e:
        print("[ERROR] Error loading Blood Bank CSV:", e)
        return pd.DataFrame()

df_blood = load_blood_banks()

# Detect columns
def detect_column(df, candidates):
    if df.empty:
        return None
    for c in candidates:
        for col in df.columns:
            if col.lower().strip() == c.lower().strip():
                return col
    return None

if not df_blood.empty:
    STATE_COL = detect_column(df_blood, ["state", "state name"])
    CITY_COL = detect_column(df_blood, ["city", "town"])
    NAME_COL = detect_column(df_blood, ["blood bank name", "name", "bank name"])
    ADDRESS_COL = detect_column(df_blood, ["address", "addr"])
    CONTACT_COL = detect_column(df_blood, ["contact", "phone", "mobile"])

    if STATE_COL:
        df_blood[STATE_COL] = df_blood[STATE_COL].astype(str).str.title()
    if CITY_COL:
        df_blood[CITY_COL] = df_blood[CITY_COL].astype(str).str.title()

    df_blood["__norm_state"] = df_blood[STATE_COL].apply(norm)
    df_blood["__norm_city"] = df_blood[CITY_COL].apply(norm)
    _all_states = sorted(df_blood[STATE_COL].dropna().unique())
else:
    STATE_COL = CITY_COL = NAME_COL = ADDRESS_COL = CONTACT_COL = None
    _all_states = []

# -----------------------------
# Base Routes
# -----------------------------
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/sopGuidelines')
def sopGuidelines():
    return render_template('sopGuidelines.html')

@main_bp.route('/emergencyContacts')
def emergencyContacts():
    return render_template('emergencyContacts.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/reportIncident')
def reportIncident():
    return render_template('reportIncident.html')

# -----------------------------
# Hydrology — Flood Prediction
# -----------------------------
@main_bp.route('/floodForecasting')
def floodForecasting():
    return render_template('floodForm.html')

@main_bp.route('/floodResults', methods=['POST', 'GET'])
def floodResults():
    if request.method == 'POST':
        if len(request.form.get('DATE', '')) == 0:
            flash("Please enter a valid date.")
            return redirect(url_for('main.floodForecasting'))
        user_date = request.form['DATE']
        river = request.form['SEL']
        results_dict = flood_predict(river, user_date)
        if results_dict is None:
            flash("No prediction data found for the selected combination. Please check input parameters.")
            return redirect(url_for('main.floodForecasting'))
        table = list(results_dict.values())
        return render_template('floodResults.html', result=table)
    return redirect(url_for('main.floodForecasting'))

# -----------------------------
# Hydrology — Rainfall Forecasting
# -----------------------------
@main_bp.route('/rainfall')
def rainfall():
    return redirect(url_for('main.rainfallAnalysis'))

@main_bp.route('/rainfallAnalysis')
def rainfallAnalysis():
    return render_template('rainfallForm.html')

@main_bp.route('/rainfallResults', methods=['POST', 'GET'])
def rainfallResults():
    if request.method == 'POST':
        year = request.form.get('Year', '')
        region = request.form.get('SEL', '')
        model_type = request.form.get('model_type', 'CNN')
        
        if len(year) == 0:
            flash("Please enter a valid year.")
            return redirect(url_for('main.rainfallAnalysis'))
            
        mae, score = predict_rainfall(year, region, model_type)
        if mae == "NIL":
            flash(f"No rainfall data available for subdivision {region} in year {year}.")
            return redirect(url_for('main.rainfallAnalysis'))
            
        return render_template('rainfallResults.html', Mae=mae, Score=score, Region=region, Year=year, ModelType=model_type)
    return redirect(url_for('main.rainfallAnalysis'))

# -----------------------------
# Medical — Blood Donation & Locator
# -----------------------------
@main_bp.route('/bloodPortal')
def bloodPortal():
    return render_template('bloodPortal.html')

@main_bp.route('/getStates')
def getStates():
    return jsonify(_all_states)

@main_bp.route('/getCities')
def getCities():
    state = request.args.get("state", "")
    if not state or df_blood.empty:
        return jsonify([])
    nstate = norm(state)
    subset = df_blood[df_blood["__norm_state"] == nstate]
    if subset.empty:
        subset = df_blood[df_blood["__norm_state"].str.contains(nstate, na=False)]
    cities = sorted(subset[CITY_COL].dropna().unique())
    return jsonify(cities[:200])

@main_bp.route('/searchBloodBanks', methods=['POST'])
def searchBloodBanks():
    if df_blood.empty:
        return jsonify({"error": "Blood bank database not loaded."}), 500
    state_raw = request.form.get("state", "").strip()
    city_raw = request.form.get("city", "").strip()

    if not state_raw or not city_raw:
        return jsonify({"error": "Please provide both state and city."}), 400

    nstate, ncity = norm(state_raw), norm(city_raw)
    subset = df_blood[df_blood["__norm_state"] == nstate]
    if subset.empty:
        subset = df_blood[df_blood["__norm_state"].str.contains(nstate, na=False)]

    if subset.empty:
        return jsonify({"error": f"No records found for state '{state_raw}'."}), 404

    matches = subset[subset["__norm_city"] == ncity]
    if matches.empty:
        matches = subset[subset["__norm_city"].str.contains(ncity, na=False)]
    if matches.empty:
        matches = subset[subset["__norm_city"].str.startswith(ncity)]

    if matches.empty:
        suggestions = sorted(subset[CITY_COL].dropna().unique())[:12]
        return jsonify({
            "error": f"No city named '{city_raw}' found in state '{state_raw}'.",
            "suggestions": suggestions
        }), 404

    results = []
    for _, row in matches.iterrows():
        results.append({
            "State": row.get(STATE_COL, ""),
            "City": row.get(CITY_COL, ""),
            "Name": row.get(NAME_COL, ""),
            "Address": row.get(ADDRESS_COL, ""),
            "Contact": row.get(CONTACT_COL, "")
        })
    return jsonify(results)
