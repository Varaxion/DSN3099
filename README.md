<div align="center">
  
	# 🌊 Sahay - Flood & Rainfall Intelligence
  
	*Hydrological forecasting, risk classification, and monthly rainfall analysis for Indian river basins and meteorological subdivisions.*
  
	<br />

	![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge)
	![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
	![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
	![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
	![ScikitLearn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

<br />

> [!NOTE]  
> **Sahay** (सहाय — *aid* in Sanskrit) was originally developed in 2024, for the **Project Exhibition - II** course at **VIT Bhopal University**. This repository contains the refactored v1.0 web application with improved UX and model caching.

---

## 📸 Application Gallery

### The First Impression
Below is the modern, dark-glassmorphic landing interface of Sahay.

<div align="center">
	<img src="screenshots/1-home.png" alt="Sahay Home Landing Hero" width="98%">
</div>

<br/>

### Feature Landing Pages
Below are the parameter input interfaces for both hydrological modules.

<div align="center">
	<img src="screenshots/4-flood-input.png" alt="Flood Prediction Parameter Selection" width="48%">
	<img src="screenshots/8-rain-input.png" alt="Rainfall Subdivision Parameter Selection" width="48%">
</div>

<br/>

### Hydrological Forecasts & CNN Outputs

<div align="center">
	<img src="screenshots/6-flood-output-graph.png" alt="Dynamic Flood Forecast Line Chart" width="48%">
	<img src="screenshots/10-rain-output-graph.png" alt="1D-CNN Rainfall Comparison Bar Chart" width="48%">
</div>

<br/>

<details>
<summary>Click here to expand the full UI walkthrough and screenshots</summary>
<br/>

### UI Walkthrough

1. Home & Navigation: landing experience, smooth transitions, and header navigation.
2. Flood Prediction Pipeline: input → loader → dynamic chart + classification table.
3. Rainfall Module: subdivision select → model load → 1D-CNN bar chart + metrics.

<br/>
</details>

---

## 🌌 Overview & System Features

Sahay v1.0 is an end-to-end Hydrological Intelligence web application engineered to predict flood risks and analyze rainfall patterns across India.

### Core highlights
- **Flood Prediction Pipeline:** ARIMA forecasting and LDA classification for major river catchments.
- **1D-CNN Rainfall Analysis:** Monthly precipitation forecasts across IMD subdivisions (1901–2021 training data).
- **Model Cache Optimization:** Cached `.h5` models per subdivision for fast loads.
- **Dynamic Charts:** Matplotlib (Agg backend) renders synchronized theme plots.
- **AJAX Blood Locator:** Searchable blood bank directory with autocomplete and click-to-call.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend UI** | HTML5, Jinja2, CSS3 | Dark glassmorphic design (`sahay.css`). |
| **Backend Engine** | Python, Flask | Flask app factory in `app/__init__.py` and routes in `app/routes.py`. |
| **Time-Series** | Statsmodels (ARIMA) | ARIMA forecasting engine. |
| **Deep Learning** | Keras, TensorFlow | 1D-CNN models stored as `.h5` in `app/trained/`. |
| **ML Classification** | Scikit-Learn | LDA with SMOTE for class balancing. |
| **Data Orchestration** | Pandas, NumPy | Data cleaning and preprocessing. |
| **Visuals** | Matplotlib | Server-side image render (Agg backend). |

---

## 📂 Project Architecture

```text
📦 DSN3099
 ┣ 📂 screenshots/         # UI screenshots
 ┣ 📂 app/
 ┃ ┣ 📂 data/              # river sheets & IMD CSVs
 ┃ ┣ 📂 static/            # CSS, JS, images, generated plots
 ┃ ┣ 📂 templates/         # Jinja2 templates
 ┃ ┣ 📂 trained/           # Cached 1D-CNN models (.h5)
 ┃ ┣ 📜 routes.py          # Flask routes & AJAX endpoints
 ┃ ┣ 📜 core/              # hydrology.py, rainfall.py (prediction logic)
 ┃ ┗ 📜 __init__.py        # App factory
 ┣ 📂 v0Archive/           # Legacy codebase and raw worksheets
 ┣ 📜 .env.example         # Sample env vars (SECRET_KEY)
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## ⚠️ Model Assumptions & Limitations

Short summary of known constraints:

- ARIMA assumes stationarity and accuracy decays with long horizons.
- LDA needs full telemetry inputs and assumes homoscedasticity.
- 1D-CNN uses monthly subdivision data and cannot predict micro-scale hourly events.

---

## 🚀 Getting Started

### 1. Set up environment

```powershell
git clone <repository-url>
cd DSN3099
python -m venv venv
venv\Scripts\Activate.ps1  # Windows PowerShell
# or on macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Copy env example

```bash
cp .env.example .env
# Edit .env and set a strong SECRET_KEY
```

### 3. Run the server (dev)

Option A (python):
```bash
python run.py
```

Option B (Flask CLI):
```bash
cd app
flask --app app run --debug
```

Open http://127.0.0.1:5000

---

## 🎓 Academic Origins & Contributors

This project began as a VIT Bhopal University academic submission (Project Exhibition - II). Major contributors:

| Name | GitHub |
| :--- | :--- |
| Kavya | https://github.com/varaxion |
| Simarpreet Singh | https://github.com/Simarpreet-2607 |
| Sneha Mishra | https://github.com/MISHSNEHA |
| Pooja | https://github.com/PrajapatPooja |

<br/>
<div align="center">
	<em>Sahay • Advancing Hydrological Safety through Intelligence.</em>
</div>

---

## DSN3099 adaptation notes

- This README is the DSN2099 blueprint adapted precisely for the DSN3099 repository (this project). All paths, commands, and examples reference DSN3099's layout: `run.py` at repo root, Flask app under `app/`, models in `app/trained/`, and data in `app/data/`.
- Cleanup status: `epicsenv/` was untracked and added to `.gitignore`; `tools/` helper script(s) were removed per project hygiene.

---

If this exact format looks good, I will mark the blueprint task completed and continue by adding a `.env.example` and a short `CONTRIBUTING.md` template. If you want any small wording changes (team credits, wording, or removal/addition of screenshots), tell me which lines to change and I will update immediately.
