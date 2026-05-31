<div align="center">

<img src="app/static/images/logo.svg" width="80" height="80" alt="Sahay Logo" style="margin-bottom: 16px;" />

# Sahay
### Predictive Disaster Intelligence & Rapid Emergency Response

*Advanced hydrological forecasting, rainfall analysis, blood bank locator, emergency guidelines, and incident-reporting simulation for public safety and preparedness.*

<br />

![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge&color=00e5ff)
![Status](https://img.shields.io/badge/Status-Archived-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
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

<details open>
<summary><b>Click to Expand/Collapse Table of Contents</b></summary>
<br>

- 🌍 [**Overview**](#-overview)
- ✨ [**Core Features**](#-core-features)
- 📸 [**Screenshots**](#-screenshots)
- 🛠️ [**Technology Stack**](#️-technology-stack)
- 📂 [**Project Architecture**](#-project-architecture)
- ⚙️ [**How the System Works**](#️-how-the-system-works)
- 🚀 [**Getting Started**](#-getting-started)
- ⚠️ [**Limitations & Assumptions**](#️-limitations--assumptions)
- 📚 [**Data Sources**](#-data-sources)
- 📄 [**License**](#-license)
- 🎓 [**Academic Origins & Credits**](#-academic-origins--credits)

</details>

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

- **Flood Prediction (ARIMA + LDA):** Forecasts water-level metrics for major rivers (Cauvery, Godavari, Krishna, Mahanadi, Son) and classifies real-time flood risk using Machine Learning.
- **Rainfall Analysis (1D-CNN + RF):** Predicts April-December monthly rainfall for Indian meteorological subdivisions using either a cached Deep Learning CNN or a Random Forest Regressor.
- **Blood Assistance Portal:** A lightning-fast, AJAX-powered locator to find local blood bank records by state and city, complete with copy actions, direct dialers, and donor eligibility guidelines.
- **Emergency Contacts:** A quick-dial public safety directory for Police, Ambulance, Fire, NDRF, NDMA, and Women Helplines.
- **Interactive Disaster SOPs:** Actionable, tabbed do's and don'ts checklists for Floods, Earthquakes, Cyclones, Landslides, Tsunamis, Wildfires, and Thunderstorms.
- **Incident Reporting Simulator:** A visually engaging prototype workflow simulating emergency dispatch routing and coordinate generation.

---

## 📸 Screenshots

### Platform Preview
![Homepage Landing](screenshots/1-homepage/homepage-1-landing.png)

<br>

### Core Features
<div align="center">

| Flood Forecasting | Rainfall Analysis |
| :---: | :---: |
| ![Flood Prediction](screenshots/2-flood-forecasting/flood-forecasting-1-landing-input.png) | ![Rainfall Prediction](screenshots/3-rainfall-analysis/rainfall-analysis-1-landing-input.png) |
| **Blood Bank Locator** | **Disaster SOPs** |
| ![Blood Locator](screenshots/4-blood-locator/blood-locator-3-locate-input.png) | ![SOPs](screenshots/5-disaster-sops/disaster-sops-1-landing.png) |
| **Incident Reporting** | **About** |
| ![Incident](screenshots/7-incident-reporting/incident-reporting-1-landing.png) | ![About](screenshots/8-about/about-1-landing.png) |

</div>

<br>
<details>
<summary><b>Click to view all detailed screenshots (Module-wise)</b></summary>
<br>

#### 1. Home
- ![Homepage Landing](screenshots/1-homepage/homepage-1-landing.png)
- ![Home Features](screenshots/1-homepage/homepage-2-features.png)
- ![Home End](screenshots/1-homepage/homepage-3-end.png)

#### 2. Flood Prediction
- ![Flood Landing Input](screenshots/2-flood-forecasting/flood-forecasting-1-landing-input.png)
- ![Flood Processing](screenshots/2-flood-forecasting/flood-forecasting-2-process.png)
- ![Flood Chart](screenshots/2-flood-forecasting/flood-forecasting-3-output-chart.png)
- ![Flood Metrics](screenshots/2-flood-forecasting/flood-forecasting-4-output-metric.png)

#### 3. Rainfall Analysis
- ![Rainfall Landing Input](screenshots/3-rainfall-analysis/rainfall-analysis-1-landing-input.png)
- ![Rainfall Processing](screenshots/3-rainfall-analysis/rainfall-analysis-2-process.png)
- ![CNN Chart](screenshots/3-rainfall-analysis/rainfall-analysis-3-cnn-output-chart.png)
- ![CNN Metric](screenshots/3-rainfall-analysis/rainfall-analysis-4-cnn-output-metric.png)
- ![Random Forest Chart](screenshots/3-rainfall-analysis/rainfall-analysis-5-randomforest-output-chart.png)
- ![Random Forest Metric](screenshots/3-rainfall-analysis/rainfall-analysis-6-randomforest-output-metric.png)

#### 4. Blood Assistance
- ![Blood Eligibility Input](screenshots/4-blood-locator/blood-locator-1-landing-eligibility-input.png)
- ![Blood Eligibility Result](screenshots/4-blood-locator/blood-locator-2-eligibility-result.png)
- ![Blood Locate Input](screenshots/4-blood-locator/blood-locator-3-locate-input.png)
- ![Blood Locate Result](screenshots/4-blood-locator/blood-locator-4-locate-result.png)

#### 5. SOPs & Helplines
- ![SOP Landing](screenshots/5-disaster-sops/disaster-sops-1-landing.png)
- ![SOP Guideline](screenshots/5-disaster-sops/disaster-sops-2-guideline.png)
- ![Emergency Helplines 1](screenshots/6-emergency-contacts/emergency-contacts-1-landing.png)
- ![Emergency Helplines 2](screenshots/6-emergency-contacts/emergency-contacts-2.png)

#### 6. Incident Reporting
- ![Incident Landing](screenshots/7-incident-reporting/incident-reporting-1-landing.png)
- ![Incident Input](screenshots/7-incident-reporting/incident-reporting-2-input.png)
- ![Incident Details](screenshots/7-incident-reporting/incident-reporting-3-details.png)
- ![Incident Process](screenshots/7-incident-reporting/incident-reporting-4-process.png)
- ![Incident Output](screenshots/7-incident-reporting/incident-reporting-5-output.png)

#### 7. About & System
- ![About Landing](screenshots/8-about/about-1-landing.png)
- ![About Technical](screenshots/8-about/about-2-technical.png)
- ![About Modules](screenshots/8-about/about-3-modules.png)
- ![About Team](screenshots/8-about/about-4-team.png)
- ![404 Error](screenshots/9-error/error-404.png)

</details>

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
📦 DSN3099
 ┣ 📂 screenshots/         # High-resolution UI mockups and dashboards
 ┣ 📂 v0Archive/           # Legacy v0 source code and conceptual media
 ┣ 📂 app/                 # Modern Optimized Application (v2.0)
 ┃ ┣ 📂 core/              # Isolated Machine Learning & pipeline logic
 ┃ ┃ ┣ 📜 hydrology.py     # Flood ARIMA forecasting & LDA classification
 ┃ ┃ ┗ 📜 rainfall.py      # CNN / RF rainfall prediction pipelines
 ┃ ┣ 📂 data/              # Datasets: River workbooks, IMD rainfall, Blood banks
 ┃ ┣ 📂 static/            # Frontend assets, stylesheets, and visual graphics
 ┃ ┃ ┣ 📂 css/             # CSS design system (sahay.css)
 ┃ ┃ ┣ 📂 images/          # Brand graphics and standalone SVGs
 ┃ ┃ ┗ 📂 charts/          # Dynamic chart target outputs (flood.png, rainfall.png)
 ┃ ┣ 📂 templates/         # Modular camelCase Jinja2 HTML views (base.html, index.html, etc.)
 ┃ ┣ 📂 trained/           # Serialized model artifacts (.h5, .pkl)
 ┃ ┣ 📜 __init__.py        # Flask app factory & blueprint registration
 ┃ ┗ 📜 routes.py          # Core routing, form handling, AJAX endpoints
 ┣ 📜 .env.example         # Environment configuration template
 ┣ 📜 requirements.txt     # Python package dependencies
 ┣ 📜 run.py               # Local WSGI development server entry point
 ┗ 📜 README.md            # Project documentation & specifications
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

## 📚 Data Sources

This academic project relies on several historical and open-source datasets to power its machine learning models and locator utilities:

- **Hydrological River Data** (`Cauvery.xlsx`, `Godavari.xlsx`, etc.): Historical water level and runoff metrics sourced from the **Central Water Commission (CWC)** and **India-WRIS** (Water Resources Information System).
- **Subdivision Rainfall Data** (`imd-rainfall-2021.csv`): Historical subdivision-wise monthly rainfall metrics provided by the **Indian Meteorological Department (IMD)** (frequently hosted on Open Government Data platforms).
- **Blood Bank Directory** (`blood-banks-india.csv`): Nationwide blood bank addresses and contact details aggregated from the **Ministry of Health and Family Welfare (e-RaktKosh)** and the Open Government Data Platform India (`data.gov.in`).

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code for your own academic or personal projects.

> [!WARNING]
> **Exclusions & Third-Party Licenses:**  
> The MIT License applies **only** to the original source code. The following assets are strictly excluded:
> 1. **Datasets:** Data files in `app/data/` (CWC, IMD, e-RaktKosh) are government property and are included for demonstration purposes only.
> 2. **Academic Documents:** Reports and videos in `v0Archive/docs/` are fully copyrighted by the authors and VIT Bhopal University.
> 3. **Hyperspace Template:** The legacy template in `v0Archive/hyperspaceTemplate/` is governed by a separate **Creative Commons Attribution 3.0 Unported (CCA 3.0)** license.

---

## 🎓 Academic Origins & Credits

This repository originated as an academic project for **VIT Bhopal University** by **Team-EPICS348** as part of the **EPICS** course in 2025. The original conceptual prototype was a collaborative effort by the following team members:

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

<br /><br />

<div align="center">
  <em>Sahay - Advancing predictive intelligence for rapid emergency response.</em>
  <br /><br />
  <p style="font-size: 13px; color: #8b949e; letter-spacing: 0.5px;">&mdash; Re-engineered by Kavya &mdash;</p>
</div>
