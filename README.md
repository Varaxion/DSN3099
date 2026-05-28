<div align="center">

# Sahay - Disaster Resilience and Emergency Assistance

*Hydrological forecasting, rainfall analysis, blood bank search, emergency guidance, and incident-reporting simulation for disaster preparedness.*

<br />

![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

<br />

> [!NOTE]
> **Sahay** was originally developed in 2025 as part of the academic curriculum for the **EPICS** course at **VIT Bhopal University**. It has now been completely overhauled into a fully modern, dynamic web application, upgrading its model speed, repository structure, and visual aesthetics to state-of-the-art glassmorphic standards.

---

## 📑 Table of Contents

- [🌍 Overview](#overview)
- [✨ Core Features](#core-features)
- [🛠️ Technology Stack](#technology-stack)
- [📂 Project Architecture](#project-architecture)
- [⚙️ How the System Works](#how-the-system-works)
- [🚀 Getting Started](#getting-started)
- [⚠️ Model Assumptions & Limitations](#model-assumptions--limitations)
- [🎓 Academic Origins & Contribution](#academic-origins--contribution)

---

<a id="overview"></a>

## 🌍 Overview

**Sahay** is a Flask-based disaster resilience platform that combines hydrological intelligence with practical emergency support utilities. It helps users explore flood risk, analyze monthly rainfall patterns, locate blood banks, access emergency helplines, follow disaster SOPs, and simulate incident reporting in one unified web portal.

The active application is housed inside `app/`, with a preserved legacy prototype under `v0Archive/` to document the project's evolution.

---

<a id="core-features"></a>

## ✨ Core Features

- **Flood Prediction:** Forecasts and classifies water-level risk for Cauvery, Godavari, Krishna, Mahanadi, and Son using ARIMA forecasting and LDA classification.
- **Rainfall Analysis:** Predicts April-December monthly rainfall for Indian meteorological subdivisions using either a cached 1D-CNN model or a Random Forest model.
- **Dynamic Charts:** Generates dark-mode Matplotlib visualizations for flood discharge and rainfall comparison outputs.
- **Blood Assistance Portal:** Searches local blood bank records by state and city with autocomplete, result cards, copy actions, and call links.
- **Emergency Contacts:** Presents public safety, ambulance, fire, NDRF, and relief helplines with direct-dial actions.
- **Disaster SOPs:** Provides interactive do/don't checklists for floods, earthquakes, cyclones, landslides, tsunamis, wildfires, and thunderstorms.
- **Incident Reporting Simulator:** Demonstrates a mock hazard-reporting workflow for academic/demo purposes. It does not alert real responders.

---

<a id="technology-stack"></a>

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| Frontend | HTML5, Jinja2, CSS3, JavaScript | Responsive glassmorphic UI and client-side interactions |
| Backend | Python, Flask, Werkzeug | Routing, forms, JSON endpoints, app factory |
| Data Processing | Pandas, NumPy, openpyxl | CSV/Excel ingestion, feature extraction, preprocessing |
| Flood Forecasting | statsmodels ARIMA | Future hydrological metric generation |
| Classification | scikit-learn LDA, imbalanced-learn SMOTE | Normal/High flood-risk classification |
| Rainfall Models | TensorFlow/Keras, Random Forest | CNN and classic ML rainfall prediction |
| Visualization | Matplotlib Agg backend | Server-side chart generation |

---

<a id="project-architecture"></a>

## 📂 Project Architecture

```text
DSN3099/
|-- app/
|   |-- __init__.py              # Flask app factory
|   |-- routes.py                # Web routes, forms, AJAX endpoints
|   |-- core/
|   |   |-- hydrology.py         # Flood forecasting and classification logic
|   |   `-- rainfall.py          # CNN/RF rainfall prediction logic
|   |-- data/                    # River workbooks, IMD rainfall CSV, blood bank CSV
|   |-- static/                  # CSS, JS, images, webfonts, generated result charts
|   |-- templates/               # Jinja2 pages
|   `-- trained/                 # Cached model artifacts
|-- v0Archive/                   # Legacy prototype, old assets, reports, recordings
|-- .env.example                 # Local environment template
|-- requirements.txt             # Python dependencies
|-- README.md                    # Project documentation
`-- run.py                       # Root Flask development entry point
```

`run.py` is the local development launcher. It imports `create_app()` from `app/__init__.py`, creates the Flask application instance, and starts the server when you run `python run.py`.

---

<a id="how-the-system-works"></a>

## ⚙️ How the System Works

### Flood Prediction Pipeline

```text
River + date input
        |
        v
Read river workbook or generate ARIMA future forecasts
        |
        v
Build hydrological feature vector
        |
        v
Classify risk using LDA
        |
        v
Render metrics table and flood chart
```

### Rainfall Analysis Pipeline

```text
Subdivision + year + model input
        |
        v
Load IMD rainfall dataset
        |
        |-- CNN: load cached .h5 model or train/cache a new one
        `-- RF: train RandomForestRegressor on selected subdivision
        |
        v
Predict April-December rainfall
        |
        v
Render MAE, explained variance, and rainfall chart
```

### Blood Bank Search Pipeline

```text
Load blood_banks_india.csv at startup
        |
        v
Expose states/cities/search JSON endpoints
        |
        v
Render matching blood banks in the browser using AJAX
```

---

<a id="getting-started"></a>

## 🚀 Getting Started

### 1. Clone the Repository

```powershell
git clone <repository-url>
cd DSN3099
```

### 2. Create and Activate a Virtual Environment

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

### 4. Configure Environment Variables

```powershell
Copy-Item .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Edit `.env` and replace `SECRET_KEY` with a strong local secret.

### 5. Run the Server

```powershell
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

---

<a id="model-assumptions--limitations"></a>

## ⚠️ Model Assumptions & Limitations

- **ARIMA Forecasting:** Forecast quality depends on historical trend behavior and can degrade over longer horizons.
- **LDA Classification:** The classifier relies on hydrological feature distributions and assumes comparable covariance structure across classes.
- **Rainfall Prediction:** The CNN and Random Forest models operate on monthly subdivision-level data, not hyperlocal or hourly rainfall.
- **Runtime Outputs:** Flood and rainfall charts are written to shared image paths under `app/static/img/`, so a production deployment should make output files user/session-specific.
- **Incident Reporting:** The incident-reporting module is only a prototype simulation and does not contact emergency agencies.
- **Emergency Data:** Blood bank and helpline information should be verified before real-world use.

---

<a id="academic-origins--contribution"></a>

## 🎓 Academic Origins & Contribution

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

> [!NOTE]
> **v1.0 Overhaul:** While the initial data gathering, research support, and legacy model iterations were developed collaboratively by **Team-EPICS348**, the complete system architectural overhaul, 1D-CNN model cache integration, dynamic dark-mode Matplotlib engine, responsive glassmorphic loaders, Flask app restructuring, repository documentation, and premium v1.0 CSS design system were engineered by Kavya.

<br />

<div align="center">
  <em>Sahay - Advancing disaster resilience through practical intelligence.</em>
  <br />
  <strong>Re-engineered by Kavya</strong>
</div>
