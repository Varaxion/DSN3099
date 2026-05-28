<div align="center">

# Sahay - Disaster Resilience and Emergency Assistance

Hydrological forecasting, rainfall analysis, blood bank search, emergency guidance, and incident-reporting simulation for disaster preparedness.

<br />

![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

<br />

> [!NOTE]
> This DSN3099 repository does not include a screenshot gallery. The documentation below follows the detailed structure of the reference README, but replaces screenshot sections with complete architecture, workflow, route, data, and file-inventory documentation.

---

## Table of Contents

- [Overview](#overview)
- [What Sahay Provides](#what-sahay-provides)
- [Application Modules](#application-modules)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Complete Repository Inventory](#complete-repository-inventory)
- [Backend and ML Workflows](#backend-and-ml-workflows)
- [Routes and Endpoints](#routes-and-endpoints)
- [Data and Model Artifacts](#data-and-model-artifacts)
- [Generated Runtime Outputs](#generated-runtime-outputs)
- [Setup and Installation](#setup-and-installation)
- [Running the App](#running-the-app)
- [Known Assumptions and Limitations](#known-assumptions-and-limitations)
- [Repo Hygiene and Maintenance](#repo-hygiene-and-maintenance)
- [Academic Context](#academic-context)

---

## Overview

**Sahay** is a Flask-based disaster resilience portal built around two major ideas:

1. Use machine learning and statistical forecasting to help users explore flood and rainfall risk.
2. Keep practical emergency utilities, such as helpline information, SOP checklists, blood bank search, and a prototype incident logger, in one unified interface.

The active DSN3099 app is under `app/`. It uses a Flask app factory, a blueprint-based route layer, Jinja2 templates, static UI assets, datasets, and trained model artifacts. The legacy prototype and older template assets are preserved in `v0Archive/` for reference.

---

## What Sahay Provides

- **Flood prediction for five Indian rivers:** Cauvery, Godavari, Krishna, Mahanadi, and Son.
- **Hydrological metrics:** discharge, flood runoff, daily runoff, weekly runoff, predicted water-level state, and historical actual state when available.
- **Rainfall analysis for Indian meteorological subdivisions:** monthly rainfall comparison for April through December.
- **Two rainfall engines:** a cached 1D-CNN deep learning model and a Random Forest fallback model.
- **Dynamic chart rendering:** Matplotlib writes result charts into `app/static/img/`.
- **Blood bank locator:** AJAX search by state and city using the local CSV dataset.
- **Emergency contacts directory:** direct-dial links for major public safety helplines.
- **Disaster SOPs:** interactive guidance tabs for floods, earthquakes, cyclones, landslides, tsunamis, wildfires, and thunderstorms.
- **Incident reporting simulator:** a front-end-only prototype that generates simulated dispatch logs and local incident IDs. It does not contact real agencies.

---

## Application Modules

### 1. Flood Prediction

The flood workflow lets a user select a river and date. For historical dates, the app reads the river workbook directly. For future dates, it creates ARIMA forecasts for the required hydrological features and then classifies the result as `Normal` or `High`.

Main files:

- `app/core/hydrology.py`
- `app/templates/floodForm.html`
- `app/templates/floodResults.html`
- `app/data/*.xlsx`
- `app/static/img/flood.png`

### 2. Rainfall Analysis

The rainfall workflow lets a user select a subdivision, year, and model type. The CNN path trains or loads a cached Keras model per subdivision. The Random Forest path trains a scikit-learn regressor at request time using the active IMD rainfall dataset.

Main files:

- `app/core/rainfall.py`
- `app/templates/rainfallForm.html`
- `app/templates/rainfallResults.html`
- `app/data/imd_rainfall_2021.csv`
- `app/trained/rainfall_cnn_*.h5`
- `app/static/img/rainfall.png`

### 3. Blood Assistance Portal

The blood portal loads `blood_banks_india.csv`, normalizes state and city names, exposes state/city lookup endpoints, and renders matching blood-bank cards in the browser through AJAX.

Main files:

- `app/routes.py`
- `app/templates/bloodPortal.html`
- `app/static/js/bloodBanks.js`
- `app/data/blood_banks_india.csv`

### 4. Emergency Guidance

The emergency support pages are mostly Jinja/CSS-driven pages with client-side interactivity for tabs, copy buttons, and simulated dispatch state.

Main files:

- `app/templates/sopGuidelines.html`
- `app/templates/emergencyContacts.html`
- `app/templates/reportIncident.html`
- `app/templates/about.html`
- `app/templates/base.html`
- `app/static/css/sahay.css`

---

## Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| Web framework | Flask, Werkzeug | App factory, routing, forms, JSON endpoints |
| Templates | Jinja2, HTML5 | Server-rendered pages |
| Styling | CSS3, bundled Font Awesome assets, legacy Sass source | Glassmorphic UI system and responsive layouts |
| Client scripts | JavaScript, Fetch API | Blood bank AJAX search, UI interactions, prototype incident simulator |
| Data handling | Pandas, NumPy, openpyxl | CSV and Excel ingestion, preprocessing, feature extraction |
| Flood forecasting | statsmodels ARIMA | Future hydrological feature generation |
| Flood classification | scikit-learn LDA, imbalanced-learn SMOTE | Normal/High risk classification |
| Rainfall CNN | TensorFlow, Keras | 1D-CNN monthly rainfall prediction |
| Rainfall RF | scikit-learn RandomForestRegressor | Classic ML rainfall prediction option |
| Visualization | Matplotlib Agg backend | Server-side chart image generation |

---

## Project Architecture

```text
DSN3099/
|-- app/
|   |-- __init__.py                  # Flask app factory and secret-key setup
|   |-- routes.py                    # Blueprint routes, forms, AJAX endpoints
|   |-- core/
|   |   |-- __init__.py              # Core prediction package marker
|   |   |-- hydrology.py             # ARIMA flood forecasting and LDA classification
|   |   `-- rainfall.py              # CNN/RF rainfall prediction and chart rendering
|   |-- data/
|   |   |-- blood_banks_india.csv    # Blood bank search dataset
|   |   |-- imd_rainfall_2021.csv    # IMD subdivision rainfall dataset
|   |   |-- Cauvery.xlsx             # River hydrology workbook
|   |   |-- Godavari.xlsx            # River hydrology workbook
|   |   |-- Krishna.xlsx             # River hydrology workbook
|   |   |-- Mahanadi.xlsx            # River hydrology workbook
|   |   `-- Son.xlsx                 # River hydrology workbook
|   |-- static/
|   |   |-- css/                     # Active compiled CSS and vendor CSS
|   |   |-- images/                  # UI images and disaster illustrations
|   |   |-- img/                     # Runtime chart targets: flood.png, rainfall.png
|   |   |-- js/                      # Front-end scripts and legacy template helpers
|   |   |-- sass/                    # Sass source from the base visual template
|   |   `-- webfonts/                # Font Awesome font files
|   |-- templates/                   # Jinja2 pages
|   `-- trained/                     # Cached model artifacts
|-- v0Archive/                       # Preserved legacy prototype and old assets
|-- .env.example                     # Sample local environment variables
|-- .gitignore                       # Ignore rules for envs, caches, generated outputs
|-- README.md                        # Project documentation
|-- requirements.txt                 # Python dependencies
`-- run.py                           # Local application entry point
```

---

## Complete Repository Inventory

### Root Files

| File | Role |
| :--- | :--- |
| `.gitignore` | Keeps virtual environments, caches, secrets, logs, and generated forecast CSVs out of Git. |
| `.env.example` | Template for local environment configuration. |
| `README.md` | Main project guide and technical documentation. |
| `requirements.txt` | Pinned Python dependency list for Flask, ML, plotting, and data libraries. |
| `run.py` | Creates the Flask app with `create_app()` and runs the development server. |

### Active Python Application Files

| File | Role |
| :--- | :--- |
| `app/__init__.py` | Defines `create_app()`, configures `SECRET_KEY`, and registers the main blueprint. |
| `app/routes.py` | Owns all page routes, form handlers, blood-bank dataset loading, state/city JSON endpoints, and search responses. |
| `app/core/__init__.py` | Makes the prediction core explicit as a package. |
| `app/core/hydrology.py` | Reads river workbooks, fills missing values, runs ARIMA forecasts, trains LDA classification with SMOTE balancing, and renders flood charts. |
| `app/core/rainfall.py` | Reads rainfall CSV data, trains/loads CNN models, trains Random Forest models, computes MAE and explained variance, and renders rainfall charts. |

### Active Jinja Templates

| File | Page |
| :--- | :--- |
| `app/templates/base.html` | Shared layout, navigation, footer, flash messages, global scripts, and base CSS import. |
| `app/templates/index.html` | Home dashboard with cards for the six major modules. |
| `app/templates/floodForm.html` | River/date input form for flood prediction. |
| `app/templates/floodResults.html` | Flood metrics table and generated discharge chart. |
| `app/templates/rainfallForm.html` | Rainfall subdivision/year/model input form. |
| `app/templates/rainfallResults.html` | Rainfall MAE, explained variance, and generated chart. |
| `app/templates/bloodPortal.html` | Blood compatibility guide, eligibility checker, and blood-bank search UI. |
| `app/templates/sopGuidelines.html` | Disaster SOP tab interface and checklist content. |
| `app/templates/emergencyContacts.html` | Helpline cards with direct dial and copy actions. |
| `app/templates/reportIncident.html` | Prototype hazard-reporting simulator. |
| `app/templates/about.html` | Technical summary, module overview, and team section. |

### Active Data Files

| File | Contents |
| :--- | :--- |
| `app/data/blood_banks_india.csv` | Local blood-bank records with name, address, city, state, contact, and helpline fields. |
| `app/data/imd_rainfall_2021.csv` | IMD rainfall subdivision data with monthly, seasonal, and annual rainfall columns. |
| `app/data/Cauvery.xlsx` | Hydrological time series for Cauvery. |
| `app/data/Godavari.xlsx` | Hydrological time series for Godavari. |
| `app/data/Krishna.xlsx` | Hydrological time series for Krishna. |
| `app/data/Mahanadi.xlsx` | Hydrological time series for Mahanadi. |
| `app/data/Son.xlsx` | Hydrological time series for Son. |

### Active Model Artifacts

| Pattern | Meaning |
| :--- | :--- |
| `app/trained/*_LDA.pkl` | Legacy/pretrained LDA classifiers by river. The active hydrology code currently retrains LDA during prediction. |
| `app/trained/*_prophet.pkl` | Legacy Prophet-style hydrology artifacts preserved with the active app assets. The current code uses ARIMA instead. |
| `app/trained/rainfall_cnn_tamil_nadu.h5` | Cached Keras CNN model for Tamil Nadu. |
| `app/trained/rainfall_cnn_east_madhya_pradesh.h5` | Cached Keras CNN model for East Madhya Pradesh. |
| `app/trained/rainfall_cnn_<subdivision>.h5` | Additional CNN cache files are created on demand when new subdivisions are analyzed. |

### Active Static Assets

| Path | Contents |
| :--- | :--- |
| `app/static/css/sahay.css` | Primary DSN3099 visual system. |
| `app/static/css/main.css`, `noscript.css`, `rainfallPrediction.css`, `fontawesome-all.min.css` | Legacy/template CSS and vendor support styles. |
| `app/static/css/images/intro.svg` | Template background/vector asset. |
| `app/static/js/bloodBanks.js` | Blood-bank lookup, autocomplete, AJAX search, card rendering, copy/call actions. |
| `app/static/js/*.js` | Bundled template utilities: jQuery, scrolly, scrollex, breakpoints, browser helpers, main UI script. |
| `app/static/img/flood.png` | Runtime output target for flood chart rendering. |
| `app/static/img/rainfall.png` | Runtime output target for rainfall chart rendering. |
| `app/static/images/Sahay.jpg` | Sahay image asset. |
| `app/static/images/emergency_contacts_images/*.jpg` | Emergency contact themed images. |
| `app/static/images/rainfall_image/rainfall.png` | Rainfall page image asset. |
| `app/static/images/sample_images/*.jpg` | Legacy/sample template images. |
| `app/static/images/sop/*.png` | SOP disaster category images. |
| `app/static/sass/**` | Sass source files from the underlying UI template. |
| `app/static/webfonts/**` | Font Awesome webfont formats. |

### Legacy Archive

`v0Archive/` preserves the older prototype. It includes:

- `v0Archive/app.py`: legacy Flask entry point.
- `v0Archive/rainfall_analysis.py`: older rainfall analysis logic.
- `v0Archive/templates/`: older page templates.
- `v0Archive/static/`: legacy CSS, JS, images, Sass, and webfonts.
- `v0Archive/hyperspaceTemplate/`: original template package files.
- `v0Archive/rainfallData/Sub_Division_IMD_2021.csv`: legacy rainfall CSV.
- `v0Archive/docs/`: project report, syllabus, and recording artifacts.

---

## Backend and ML Workflows

### Flood Prediction Flow

```text
User selects river and date
        |
        v
/floodResults POST handler
        |
        v
app.core.hydrology.drive(river, date)
        |
        |-- Historical date:
        |      read river workbook
        |      fill missing feature values
        |      train LDA classifier on historical split
        |      classify selected date
        |      render discharge chart to app/static/img/flood.png
        |
        `-- Future date:
               run ARIMA forecasts for discharge/runoff features
               save forecast CSVs under app/data/forecast/
               align daily and weekly feature series
               classify forecasted feature vector
               render forecast chart to app/static/img/flood.png
```

### Rainfall Analysis Flow

```text
User selects model, subdivision, and year
        |
        v
/rainfallResults POST handler
        |
        v
app.core.rainfall.predict_rainfall(year, region, model_type)
        |
        |-- CNN:
        |      read imd_rainfall_2021.csv
        |      load cached app/trained/rainfall_cnn_<region>.h5 if present
        |      otherwise train a Conv1D model and cache it
        |      predict April-December values
        |      compute MAE and explained variance
        |
        `-- RF:
               read imd_rainfall_2021.csv
               train RandomForestRegressor for selected subdivision
               predict April-December values
               compute MAE and explained variance

        |
        v
Render chart to app/static/img/rainfall.png
```

### Blood Bank Search Flow

```text
App startup loads app/data/blood_banks_india.csv
        |
        v
/getStates returns distinct states
/getCities?state=... returns city suggestions
/searchBloodBanks POST returns matching centers
        |
        v
app/static/js/bloodBanks.js renders result cards
```

---

## Routes and Endpoints

| Route | Method | Purpose |
| :--- | :--- | :--- |
| `/` | GET | Home page. |
| `/about` | GET | Project and team information. |
| `/floodForecasting` | GET | Flood prediction input form. |
| `/floodResults` | GET/POST | POST runs flood prediction; GET redirects back to the form. |
| `/rainfall` | GET | Redirects to `/rainfallAnalysis`. |
| `/rainfallAnalysis` | GET | Rainfall input form. |
| `/rainfallResults` | GET/POST | POST runs rainfall analysis; GET redirects back to the form. |
| `/bloodPortal` | GET | Blood assistance and search UI. |
| `/getStates` | GET | JSON list of available states from the blood-bank CSV. |
| `/getCities` | GET | JSON city suggestions for a selected state. |
| `/searchBloodBanks` | POST | JSON blood-bank matches for state and city. |
| `/sopGuidelines` | GET | Disaster SOP checklist page. |
| `/emergencyContacts` | GET | Emergency contacts directory. |
| `/reportIncident` | GET | Prototype incident-reporting simulator. |

---

## Data and Model Artifacts

### River Workbook Expectations

Each river workbook is expected to contain a `Date` column and hydrological feature columns used by `hydrology.py`, including:

- `Discharge`
- `flood runoff`
- `daily runoff`
- `weekly runoff`
- `Flood`

The `Flood` column is converted into a binary class. Values greater than or equal to `0.1` are treated as `High`; lower values are treated as `Normal`.

### Rainfall CSV Expectations

`app/data/imd_rainfall_2021.csv` is expected to contain:

- `SUBDIVISION`
- `YEAR`
- Monthly columns from `JAN` through `DEC`
- Seasonal and annual aggregate columns such as `ANNUAL`, `JF`, `MAM`, `JJAS`, and `OND`

The active CSV currently has the column structure required by both the CNN and Random Forest rainfall engines.

### Blood Bank CSV Expectations

`app/data/blood_banks_india.csv` is expected to contain:

- `Blood Bank Name`
- `Address`
- `City`
- `State`
- `Contact`
- `Helpline`

`routes.py` normalizes column names to lowercase and dynamically detects contact/name/address fields where possible.

---

## Generated Runtime Outputs

The app writes a few files during normal operation:

| Path | Generated By | Purpose |
| :--- | :--- | :--- |
| `app/static/img/flood.png` | `plot_flood_graph()` | Latest flood result chart displayed in `floodResults.html`. |
| `app/static/img/rainfall.png` | `plot_rainfall_graph()` | Latest rainfall chart displayed in `rainfallResults.html`. |
| `app/data/forecast/*.csv` | ARIMA forecast functions | Future hydrology forecast tables. Ignored by Git. |
| `app/trained/rainfall_cnn_<region>.h5` | CNN rainfall engine | Cached trained model for newly queried subdivisions. |

Because `flood.png` and `rainfall.png` are overwritten per request, this app is best treated as a local academic/demo application unless chart output paths are made user/session-specific.

---

## Setup and Installation

### 1. Clone and Enter the Project

```powershell
git clone <repository-url>
cd DSN3099
```

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

> [!TIP]
> TensorFlow can be large and platform-sensitive. If installation fails, first upgrade packaging tools with `python -m pip install --upgrade pip setuptools wheel`, then retry the requirements installation.

### 4. Configure Local Environment

```powershell
Copy-Item .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Edit `.env` and replace `SECRET_KEY` with a strong local secret.

---

## Running the App

### Recommended

```powershell
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

### Flask CLI Alternative

```powershell
$env:FLASK_APP="run.py"
flask run --debug
```

On macOS/Linux:

```bash
export FLASK_APP=run.py
flask run --debug
```

---

## Known Assumptions and Limitations

### Flood Model

- ARIMA assumes the time series can be modeled through historical trend and differencing behavior.
- Long-horizon forecasts accumulate uncertainty.
- The LDA classifier assumes comparable feature distributions and equal covariance structure between classes.
- Future-date predictions do not have actual flood labels, so `actualFlood` is displayed as `NIL`.
- The current implementation retrains some model components during requests, which is acceptable for demos but not ideal for production latency.

### Rainfall Model

- The CNN and Random Forest engines operate on monthly subdivision data, not hyperlocal hourly rainfall.
- The prediction view compares April through December values generated from rolling three-month windows.
- CNN cache files are created per subdivision; first run for a new subdivision can be slower.
- The dataset ends at 2021, so the current UI restricts rainfall years to 1901-2021.

### Emergency and Medical Modules

- Blood-bank information is only as current as the bundled CSV.
- Emergency contacts are static content and should be verified before real-world use.
- The incident-reporting module is a simulation only. It does not store reports on a server or notify responders.

### Deployment

- The app uses local file writes for generated charts and forecast CSVs.
- For multi-user hosting, generated chart paths should be made unique per request or per session.
- A production deployment should remove debug mode, set a strong secret key, add request validation, and place large model/data files behind a proper artifact strategy.

---

## Repo Hygiene and Maintenance

Recent structure improvements:

- Added `.env.example` because the README and Flask config expect local environment variables.
- Added `app/core/__init__.py` so prediction modules are clearly packaged.
- Cleaned `.gitignore` to remove duplicates and ignore virtual environments, caches, secrets, generated forecasts, and optional screenshots.
- Removed tracked Python bytecode cache files from the repo.
- Updated the Random Forest rainfall engine to use the active `app/data/imd_rainfall_2021.csv` dataset.
- Replaced the previous screenshot-based README with a screenshot-free DSN3099 guide.

Recommended future cleanup:

- Move legacy template assets that are not used by the active app fully under `v0Archive/`.
- Add tests for the route handlers and the data-loading helpers.
- Add session-specific output filenames for generated charts.
- Decide whether legacy `.pkl` artifacts in `app/trained/` should stay active or move into `v0Archive/trained/`.
- Consider storing large model files through Git LFS or a release artifact workflow.

---

## Academic Context

Sahay was developed as an academic disaster-management and hydrological-intelligence project for VIT Bhopal University.

The current DSN3099 version identifies the team as **EPICS348** in the app UI.

| Name | Registration No. |
| :--- | :--- |
| Chelsi Patel | `22BAI10005` |
| Aditya Nayak | `22BAI10424` |
| Rushabh Wagh | `22BCE10364` |
| Kavya | `22BCE10385` |
| Tejas Pathak | `22BCE10853` |
| Simarpreet Singh | `22BCE10914` |
| Sneha Mishra | `22BCE10932` |
| Pooja | `22BCE10984` |
| Ruturaj Bhoite | `22BHI10027` |
| Archana Nair | `22BSA10238` |

<br />

<div align="center">
  <em>Sahay - Advancing disaster resilience through practical intelligence.</em>
</div>
