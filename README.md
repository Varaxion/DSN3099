# Sahay — Flood & Rainfall Intelligence

Sahay is an academic-origin hydrological intelligence web application focused on flood forecasting, rainfall prediction, and emergency support utilities for Indian river basins and meteorological subdivisions.

---

## Table of Contents
- Project overview
- Features
- Tech stack
- Data & models
- Local setup
- Running the app
- File layout
- SOP & UX notes
- Cleanup actions applied
- Recommendations
- Contributors

## Project overview

Sahay combines statistical time-series forecasting (ARIMA), classical ML (Random Forest, LDA), and deep learning (1D-CNN) engines to provide:

- Flood risk forecasts and classification for multiple river basins (Cauvery, Godavari, Krishna, Mahanadi, Son).
- Monthly rainfall forecasts for IMD subdivisions using both CNN and Random Forest approaches.
- A searchable AJAX blood-bank directory and emergency contacts dashboard.
- Actionable SOP checklists (Do's and Don'ts) for various hazards with print/export UX controls.

## Features (details)

- Flood forecasting: Uses resampled station data and ARIMA forecasting for short-term predictions; results are exported to `app/static/img/flood.png` and CSV outputs under `app/static/data/`.
- Flood classification: LDA-based classifier (SMOTE oversampled during training) that assigns risk labels like `Normal` or `High`.
- Rainfall prediction: Two engines — `cnn_predict_rainfall` (loads CNN `.h5`) and `rf_predict_rainfall` (RandomForestRegressor). A toggle in the UI selects the engine.
- Blood bank portal: AJAX endpoints (`/searchBloodBanks`, `/getStates`, `/getCities`) with client-side autocomplete and click-to-call actions.
- SOPs: Checklist UI with collapsible sections and print/export controls (now refined per design request).

## Tech stack

- Backend: Flask (application factory in `app/__init__.py`, routes in `app/routes.py`).
- ML: Keras (model `.h5`), TensorFlow runtime (add to `requirements.txt`), scikit-learn, imbalanced-learn (SMOTE), statsmodels (ARIMA).
- Data: pandas, numpy, openpyxl for XLSX.
- Plotting: matplotlib (Agg) for server-side image generation.

## Data & models

- Active datasets: `app/data/` (includes `blood_banks_india.csv`, IMD rainfall CSVs, and river workbooks).
- Trained models: `app/trained/` contains `.h5` and pickle files. These are large — consider storing them in releases or external object storage.
- Note: Keras requires a matching TensorFlow version. We appended `tensorflow>=2.12.0` to `requirements.txt` to align with `keras==3.x` usage.

## Local setup

1. Create & activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1  # Windows PowerShell
# or on Unix
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Environment variables:

- Set `SECRET_KEY` for Flask (recommended) via `.env` or your environment. Create `.env.example` for documentation.

## Running the app (development)

```bash
python run.py
# Open http://127.0.0.1:5000
```

Notes:
- `run.py` is a small launcher that calls `app.create_app()` — suitable for local testing. For production, run behind Gunicorn or another WSGI server and disable debug mode.

## File layout

```
app/                # Flask package (routes, templates, static, core)
	core/             # hydrology.py, rainfall.py (prediction logic)
	data/             # CSV / XLSX inputs
	trained/          # model weights (.h5) and pickles
	templates/        # Jinja2 templates including SOPs
	static/           # CSS, JS, images, generated charts
v0Archive/          # Legacy assets and original project snapshot
run.py              # Local dev launcher
requirements.txt    # Python dependencies
.gitignore          # Ignored files
```

## SOP & UX notes

- SOPs are presented as action-oriented checklists with clear Do's and Don'ts. The page includes print/export controls and improved iconography for clarity.
- Recent UI change: removed collapsible behavior on some items per stakeholder request and refined the About page language.

## Cleanup actions applied

- Removed tracked `epicsenv/` virtualenv from Git and added it to `.gitignore` (to avoid repository bloat).
- Removed `tools/` helper script(s) at your request.
- Appended `tensorflow>=2.12.0` to `requirements.txt` to support Keras model loading.

## Recommendations & next steps

1. If you want repository size reduced further, consider removing model binaries from history (use BFG or git filter-repo) and store models externally.
2. Create `.env.example` and add `SECRET_KEY` to it; keep real secrets out of Git.
3. Optionally exclude `app/trained/*.h5` from Git and publish models as release assets.
4. Review duplicates reported earlier and decide canonical locations; I can run an automated move to `v0Archive/` on approval.

## Contributors

- Kavya — https://github.com/varaxion
- Aditya — https://github.com/adi152003
- Archana — https://github.com/Archana-P-Nair
- Chelsi — https://github.com/Chelsi08
- Sneha — https://github.com/MISHSNEHA
- Pooja — https://github.com/PrajapatPooja
- Ruturaj — https://github.com/Ranazaur
- Simarpreet — https://github.com/Simarpreet-2607
- Tejas — https://github.com/tejas-0-5
- Rushabh — https://github.com/wrexrus

---

If you'd like further expansion (detailed API docs for endpoints, CLI examples, or a CONTRIBUTING guide), tell me which section to expand and I'll add it.