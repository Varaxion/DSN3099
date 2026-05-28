# 🌊 Sahay — Flood & Rainfall Intelligence

Hydrological forecasting, flood-risk classification, and monthly rainfall analysis across Indian river basins and meteorological subdivisions.

---

## ✨ Highlights
- ARIMA-based flood forecasting and LDA risk classification for major river basins.
- 1D-CNN and Random Forest rainfall prediction engines.
- AJAX blood-bank directory and searchable emergency contacts.
- Actionable SOP checklists for floods, earthquakes, cyclones, landslides, and more.

## 🚀 Quick start
1. Create & activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run in development:

```bash
python run.py
# open http://127.0.0.1:5000
```

Notes:
- `run.py` is a local development launcher that calls `app.create_app()`.
- Set `SECRET_KEY` via environment variable for production and do not use `debug=True`.

## 🗂 Important files
```
app/             # Flask package (routes, templates, static, core)
app/data/        # Active datasets (CSV / XLSX)
app/trained/     # Model weights (.h5) and pickles
v0Archive/       # Legacy backups and original assets
run.py           # Development launcher
requirements.txt # Python dependencies (includes TensorFlow)
.gitignore       # Ignored files (virtualenvs, env files, screenshots)
```

## ✅ Cleanup actions applied
- Added `.gitignore` and untracked the committed virtualenv `epicsenv/`.
- Removed `tools/` helper scripts (per request).
- Appended `tensorflow>=2.12.0` to `requirements.txt` to match Keras usage.

## ⚙️ Recommendations
- Keep large model artifacts (`app/trained/*.h5`) out of Git; use release artifacts or object storage.
- Add `.env.example` with required env vars (`SECRET_KEY`).
- For production, run behind a WSGI server (Gunicorn/uvicorn).

## 🧩 Contributors
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

If you want, I can now run the `git` commands to remove `epicsenv` from the index, commit these housekeeping changes, and push them to `origin/main`.