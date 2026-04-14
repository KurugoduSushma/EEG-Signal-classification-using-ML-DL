# EEG Classification Frontend

Simple Flask frontend for EEG signal classification (templates + static assets).

Quick start (local):

1. Create & activate a Python virtual environment.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# or cmd
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
# for development
python app.py

# or use gunicorn (production-like)
gunicorn app:app
```

Deployment:

- Run locally using the Quick start instructions above. The app uses a local SQLite database by default (file `app.db` in the `FRONTEND` folder). To override the DB file path, set the `DB_PATH` environment variable to an absolute path.

Model & storage notes:

- Large model files are ignored by `.gitignore`. Upload your trained models to a cloud storage (S3, GCS) or Render Disk and update `MODEL_PATH` in `app.py` accordingly.
- Avoid committing sensitive files (passwords, DB dumps).

If you want, I can initialize a Git repo and push this `FRONTEND` folder to GitHub for you.