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

Render deployment notes:

- A `Procfile` is included (`web: gunicorn app:app`).
- Push this folder to a GitHub repo, then create a Web Service on render.com.
- On Render set the build command to `pip install -r requirements.txt` and the start command to `gunicorn app:app`.
- Configure environment variables on Render for your database credentials instead of hardcoding them in `app.py`.

Model & storage notes:

- Large model files are ignored by `.gitignore`. Upload your trained models to a cloud storage (S3, GCS) or Render Disk and update `MODEL_PATH` in `app.py` accordingly.
- Avoid committing sensitive files (passwords, DB dumps).

If you want, I can initialize a Git repo and push this `FRONTEND` folder to GitHub for you.