<div align="center">

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/shield-halved.svg" width="80" height="80" alt="Sahay Logo" style="filter: drop-shadow(0 0 10px rgba(0, 229, 255, 0.5));" />

# Sahay
### Disaster Resilience & Emergency Assistance Portal

*Advanced hydrological forecasting, rainfall analysis, blood bank locator, emergency guidelines, and incident-reporting simulation for public safety and preparedness.*

<br />

![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge&color=00e5ff)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

<br />

> [!NOTE]
> **Sahay** was originally developed in 2025 as part of the academic curriculum for the **EPICS** course at **VIT Bhopal University**. It has now been completely overhauled into a modern, dynamic web application, upgrading its model speed, repository structure, and visual aesthetics to state-of-the-art glassmorphic standards.

---

## 📑 Table of Contents

- [🌍 Overview](#-overview)
- [✨ Core Features](#-core-features)
- [📸 Screenshots](#-screenshots)
- [🛠️ Technology Stack](#-technology-stack)
- [📂 Project Architecture](#-project-architecture)
- [⚙️ How the System Works](#-how-the-system-works)
- [🚀 Getting Started](#-getting-started)
- [⚠️ Limitations & Assumptions](#-limitations--assumptions)
- [🎓 Academic Origins & Credits](#-academic-origins--credits)

---

## 🌍 Overview

**Sahay** is a comprehensive Flask-based disaster resilience platform that fuses machine-learning hydrological intelligence with practical, on-the-ground emergency support utilities. Designed with a stunning dark glassmorphic UI, it provides a unified hub to:
- Forecast river flood risks
- Analyze monthly subdivision rainfall patterns
- Locate life-saving blood banks
- Access direct-dial emergency helplines
- Study interactive disaster Standard Operating Procedures (SOPs)
- Simulate mock incident-reporting for training and demonstrations

*(The active v1.0 application is housed inside `app/`, while the preserved v0 legacy prototype is kept under `v0Archive/` to document the project's evolution.)*

---

## ✨ Core Features

- 🌊 **Flood Prediction (ARIMA + LDA):** Forecasts water-level metrics for major rivers (Cauvery, Godavari, Krishna, Mahanadi, Son) and classifies real-time flood risk using Machine Learning.
- 🌧️ **Rainfall Analysis (1D-CNN + RF):** Predicts April-December monthly rainfall for Indian meteorological subdivisions using either a cached Deep Learning CNN or a Random Forest Regressor.
- 🩸 **Blood Assistance Portal:** A lightning-fast, AJAX-powered locator to find local blood bank records by state and city, complete with copy actions, direct dialers, and donor eligibility guidelines.
- 🚑 **Emergency Contacts:** A quick-dial public safety directory for Police, Ambulance, Fire, NDRF, NDMA, and Women Helplines.
- 📋 **Interactive Disaster SOPs:** Actionable, tabbed do's and don'ts checklists for Floods, Earthquakes, Cyclones, Landslides, Tsunamis, Wildfires, and Thunderstorms.
- ⚠️ **Incident Reporting Simulator:** A visually engaging prototype workflow simulating emergency dispatch routing and coordinate generation.

---

## 📸 Screenshots

*(Replace these placeholders with actual project screenshots before final commit)*

<div align="center">

| Homepage Dashboard | Flood Forecasting |
| :---: | :---: |
| ![Homepage](screenshots/home.png) | ![Flood Prediction](screenshots/flood.png) |
| **Blood Bank Locator** | **Emergency SOPs** |
| ![Blood Locator](screenshots/blood.png) | ![SOPs](screenshots/sops.png) |

</div>

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend UI** | HTML5, Jinja2, Vanilla CSS3 (Glassmorphism), Vanilla JavaScript |
| **Backend Framework** | Python 3.10+, Flask, Werkzeug |
| **Data Processing** | Pandas, NumPy, openpyxl |
| **Flood Models** | `statsmodels` (ARIMA), `scikit-learn` (LDA), `imblearn` (SMOTE) |
| **Rainfall Models** | `TensorFlow/Keras` (1D-CNN), `scikit-learn` (Random Forest) |
| **Visualizations** | `Matplotlib` (Agg backend) for dynamic dark-mode server charting |

---

## 📂 Project Architecture

```text
DSN3099/
├── app/
│   ├── __init__.py              # Flask app factory & blueprint registration
│   ├── routes.py                # Core routing, form handling, AJAX endpoints
│   ├── core/                    # Isolated Machine Learning logic
│   │   ├── hydrology.py         # Flood ARIMA forecasting & LDA classification
│   │   └── rainfall.py          # CNN / RF rainfall prediction pipelines
│   ├── data/                    # Datasets: River workbooks, IMD rainfall, Blood banks
│   ├── static/                  # CSS design system, JS scripts, dynamic charts
│   ├── templates/               # Modular camelCase Jinja2 views
│   └── trained/                 # Serialized model artifacts (.h5, .pkl)
├── v0Archive/                   # Legacy v0 source code and conceptual media
├── .env.example                 # Environment configuration template
├── requirements.txt             # Python package dependencies
├── README.md                    # Project documentation
└── run.py                       # Local WSGI development server entry point
```

---

## ⚙️ How the System Works

### 1. Flood Prediction Pipeline
User inputs River & Date ➔ `hydrology.py` reads historical river workbook ➔ Generates `ARIMA` future trend ➔ Extracts structural features ➔ Passes vector to `LinearDiscriminantAnalysis` ➔ Classifies Normal vs. High Risk ➔ Renders Matplotlib chart & metrics table.

### 2. Rainfall Analysis Pipeline
User inputs Subdivision, Year & Model ➔ `rainfall.py` parses IMD dataset ➔ If **CNN**, loads cached `Keras .h5` model (or trains on-the-fly) ➔ If **RF**, trains `RandomForestRegressor` ➔ Predicts April–December mm ➔ Calculates MAE & Variance ➔ Renders comparative chart.

### 3. Blood Bank Search
`routes.py` loads `blood_banks_india.csv` globally on server start ➔ Normalizes strings (Title Case) ➔ Exposes `/getCities` and `/searchBloodBanks` JSON endpoints ➔ Client-side JS fetches and renders results instantly without page reloads.

---

## 🚀 Getting Started

### 1. Clone the Repository
```powershell
git clone https://github.com/Varaxion/DSN3099.git
cd DSN3099
```

### 2. Create and Activate a Virtual Environment
**Windows:**
```powershell
python -m venv epicsenv
.\epicsenv\Scripts\Activate.ps1
```
**macOS/Linux:**
```bash
python3 -m venv epicsenv
source epicsenv/bin/activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run the Server
```powershell
python run.py
```
*The Sahay portal will be live at `http://127.0.0.1:5000`*

---

## ⚠️ Limitations & Assumptions

- **ARIMA Horizons:** Flood forecasting relies on historical moving averages; long-term horizon accuracy decays naturally.
- **LDA Covariance:** Flood risk classification assumes equal covariance matrices across normal and high-risk classes.
- **Rainfall Granularity:** Both CNN and RF models operate on aggregated *monthly* subdivision data, not hyperlocal or daily weather metrics.
- **Incident Reporting:** The reporting module is strictly a UI prototype/simulation. It **does not** dispatch or alert real-world NDRF agencies.
- **Medical Data:** Blood bank contact numbers and addresses are sourced from open datasets and should be independently verified in a real emergency.

---

## 🎓 Academic Origins & Credits

This repository originated as an academic project for **VIT Bhopal University** (**Team-EPICS348**) as part of the **EPICS** course in 2025. The original conceptual prototype was a collaborative effort by the following team members:

| Name | Registration No. |
| :--- | :---: |
| [Chelsi Patel](https://github.com/Chelsi08) | `22BAI10005` |
| [Aditya Nayak](https://github.com/adi152003) | `22BAI10424` |
| [Rushabh Wagh](https://github.com/wrexrus) | `22BCE10364` |
| [Kavya](https://github.com/varaxion) | `22BCE10385` |
| [Tejas Pathak](https://github.com/tejas-0-5) | `22BCE10853` |
| [Simarpreet Singh](https://github.com/Simarpreet-2607) | `22BCE10914` |
| [Sneha Mishra](https://github.com/MISHSNEHA) | `22BCE10932` |
| [Pooja](https://github.com/PrajapatPooja) | `22BCE10984` |
| [Ruturaj Bhoite](https://github.com/Ranazaur) | `22BHI10027` |
| [Archana Prasad Nair](https://github.com/Archana-P-Nair) | `22BSA10238` |

> [!IMPORTANT]
> **v1.0 Overhaul:** While the initial data gathering, research support, and legacy model iterations were developed collaboratively by **Team-EPICS348**, the complete system architectural overhaul, 1D-CNN model cache integration, dynamic dark-mode Matplotlib engine, responsive glassmorphic loaders, Flask app restructuring, repository documentation, and premium v1.0 CSS design system were engineered by Kavya.

<br />

<div align="center">
  <em>Sahay - Advancing disaster resilience through practical intelligence.</em>
  <br />
  <strong>Re-engineered by Kavya</strong>
</div>
