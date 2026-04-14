# EEG Signal Classification — ML & DL

Project exploring machine learning and deep learning techniques for EEG signal classification. Includes data, notebooks, and a Flask frontend for uploading EEG CSVs and running trained models.

**Contents**
- `BACKEND/` — analysis notebook and raw dataset(s). Primary research and model training lives here.
- `FRONTEND/` — Flask app, templates, static assets, saved models (ignored in git by default), and deployment files (`Procfile`, `requirements.txt`).

**What it does**
- Trains and evaluates classifiers for EEG-based disorder classification (see `BACKEND/code.ipynb`).
- Provides a web UI to register/login, upload CSVs, and run predictions using models from `FRONTEND/eeg_saved_models/`.

**Quick start (local)**
1. Open a terminal in the project root (`CODE`).
2. Create & activate a Python virtual environment and install dependencies for the frontend (app):

```bash
cd FRONTEND
python -m venv .venv
# PowerShell
.venv\Scripts\Activate.ps1
# or cmd
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the web app for development:

```bash
python app.py
# visit http://localhost:5000
```

4. If deploying to a host (Render) use the included `Procfile`:

```text
web: gunicorn app:app
```

**Configuration**
- Database config in `FRONTEND/app.py` is set via `db_config` dictionary. For production, replace with environment variables and do NOT commit credentials.
- `MODEL_PATH` in `FRONTEND/app.py` points to `FRONTEND/eeg_saved_models/` by default — consider storing large models in cloud storage and loading them at runtime.

**Deployment**
1. Push the repository to GitHub (already done). 2. Connect the repo to Render, choose the `FRONTEND` folder as the deploy root, set the build command to `pip install -r requirements.txt` and start command to `gunicorn app:app`.

**Notes & best practices**
- Do not commit large model files or raw datasets; use cloud storage (S3/GCS) and update `MODEL_PATH` accordingly.
- Use an external DB (MySQL/Postgres) in production rather than SQLite or embedded files.
- Validate and sanitize uploaded CSVs before processing to avoid crashes.

**License & credit**
This repository is the work of the author; add a license file if you plan to publish publicly.


