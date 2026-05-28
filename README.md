# Sahay — A Hub for Disaster Resilience &amp; Emergency Assistance

Sahay is a comprehensive web application designed to build disaster resilience and provide immediate emergency assistance. Built as an academic engineering project in community service, the platform consolidates hydrological ML modeling, nationwide medical blood supply locators, direct emergency directories, dynamic SOP hazard checklists, and an AI-driven rescue chatbot into a unified, premium user interface.

---

## 🌌 Modern Features Overview

### 1. 🌊 Hydrological Forecasting
* **Dynamic Discharge Trends**: Plots 30-day river discharge charts dynamically centering around selected dates.
* **ARIMA Forecasting**: Leverages auto-regressive integrated moving average time-series models to forecast future river metrics up to late 2026.
* **LDA Classification**: Uses a trained **Linear Discriminant Analysis (LDA)** classifier (augmented via SMOTE) to categorize water levels as **Normal** or **High** with MAE precision metrics.
* **Catchments Covered**: Cauvery, Godavari, Krishna, Mahanadi, and Son systems.

### 2. 🌧️ Rainfall Forecasting
* **Dual ML Engines**: Give users a toggle choice between **1D Convolutional Neural Networks (Deep Learning)** cached weights or **Random Forest Regressors (Classic ML)** trained on the fly.
* **Precision Plotting**: Renders high-quality comparative dark-glassmorphic bar charts detailing model predictions vs. historical ground truths (1901–2021).

### 3. 🩸 AJAX Blood Locator Portal
* **8000+ Record Database**: Dynamic search engine querying government-approved blood banks across India.
* **Autonomous Suggestions**: Cached autocomplete matching for city entries as you type under normalized state lists.
* **Active Cards**: Renders interactive results showing names, addresses, and telephone details complete with click-to-copy buttons and direct click-to-call mobile links.

### 4. 🚨 Hazard Incident Reporting
* **Interactive Logger**: Glassmorphic modal form overlay allowing users to log active fires, floods, earthquakes, and landslides in real-time.
* **Rescue Transmission**: Simulates coordinates dispatch to emergency responder units and PMNRF disaster teams.

### 5. 📂 Standard Operating Procedures (SOPs)
* **Actionable Checklists**: Step-by-step Do's and Don'ts guidelines for high-alert disasters (Earthquakes, Floods, Cyclones, Landslides).

### 6. 📞 Emergency Helplines
* **Direct Directories**: Direct click-to-call action blocks for core helplines (Police, Fire Departments, PMNRF Relief, Hospitals) with localized landmark labels.

---

## 🛠️ Technology Stack
* **Web Framework**: Flask (Python 3)
* **Deep Learning**: Keras 3 &amp; TensorFlow
* **Machine Learning**: scikit-learn (SMOTE, RandomForest, LDA)
* **Statistical Analysis**: statsmodels (ARIMA)
* **Data Processing**: pandas, numpy, openpyxl
* **Data Visualizations**: matplotlib (Agg backend)
* **Frontend**: HTML5, Vanilla CSS (Hyperspace/sahay layouts), AJAX

---

## 📂 Repository Structure

The active production application utilizes a highly organized, modular Flask package format:

```
├── app/                      # Main active application package
│   ├── __init__.py           # Flask App Factory and configuration setup
│   ├── routes.py             # Central blueprint router & AJAX handlers
│   ├── core/                 # Core prediction & analytical libraries
│   │   ├── hydrology.py      # ARIMA forecasting & LDA classifier
│   │   └── rainfall.py       # Dual CNN / RF rainfall prediction engine
│   ├── data/                 # Unified databases (river sheets & blood banks CSV)
│   │   ├── blood_banks_india.csv
│   │   ├── imd_rainfall_2021.csv
│   │   ├── Sub_Division_IMD_2021.csv
│   │   └── [river].xlsx (Cauvery, Godavari, Krishna, Mahanadi, Son)
│   ├── trained/              # Model files & pickles (CNN .h5, LDA pickles)
│   ├── static/               # Assets (sahay.css, blood-banks.js, fonts, images)
│   └── templates/            # HTML templates (index, blood, flood, rainfall, about, etc.)
├── v0Archive/                # Legacy historical backups
│   ├── original_app/         # Snapshot of baseline code before refactoring
│   ├── Template/             # Raw HTML download layout folder
│   └── Screen Recording 2024-12-12 000922.mp4
├── run.py                    # Server launch entry point
├── requirements.txt          # Combined python dependencies
└── README.md                 # Project showcase
```

---

## 🚀 Local Deployment Guide

1. **Clone the Repository** and navigate to the project directory:
   ```bash
   cd DSN3099
   ```

2. **Install Core Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Unified Server**:
   ```bash
   python run.py
   ```

4. **Verify Live Access**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Data Maintenance Helpers

A small utility is included to help detect duplicate files across common data locations and optionally relocate duplicates for manual review:

```bash
python tools/deduplicate_data.py --report   # scan and report duplicates
python tools/deduplicate_data.py --move     # move detected duplicates to app/data/duplicates
```

This is safe by default (report mode). Moving duplicates preserves files by relocating them — nothing is permanently deleted.

## SOP Page Improvements

The SOP (Standard Operating Procedures) page has improved UX: collapsible checklists for each Do/Don't card, and `Print` and `Export` controls to print or download active SOPs as plain text.

---

## 🌌 Mathematical Foundations & Analytical Limits

* **ARIMA (p, d, q) Time-Series Models**: Utilizes an order configuration of `(5, 1, 0)` on resampled data. Assumes hydrological stationarity over long-term seasonal intervals. Extreme weather anomalies exceeding historic training standard deviations are bounded by model smoothing limits.
* **Linear Discriminant Analysis (LDA)**: Projects multidimensional features (discharge, runoff) to a 1D plane, separating classification boundaries. Requires balanced classes; SMOTE oversampling is applied to correct for rare, high-volume flooding anomalies in historical records.
* **1D Convolutional Neural Network (CNN)**: Conv1D layers apply kernels over a rolling 3-month precipitation window. Features are activated via rectified linear units (ReLU) and linear output regressions, assuming precipitation features depend primarily on localized seasonal transitions.

---

## 🎓 Academic Origins & Credits

Developed as an **Engineering Project in Community Service (EPICS)** at **VIT Bhopal University, 2026**:

* **Kavya** — 22BCE10385
* **Simarpreet Singh** — 22BCE10914
* **Sneha Mishra** — 22BCE10932
* **Pooja** — 22BCE10984
* **Ashish Kumar** — 22BCE11353
