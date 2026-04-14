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

Deployment / Database

- The app expects a MySQL database for user accounts. By default it reads connection info from environment variables:
	- `DB_HOST` (default: `localhost`)
	- `DB_PORT` (default: `3306`)
	- `DB_USER` (default: `root`)
	- `DB_PASS` (default: empty)
	- `DB_NAME` (default: `eeg_users`)

- For local development using XAMPP/MySQL, ensure MySQL is running and create the database (example):

```sql
CREATE DATABASE eeg_users;
```

Then start the app as described above. The application will create the `users` table on first run if it does not exist.

Model & storage notes:

- Large model files are ignored by `.gitignore`. Upload your trained models to a cloud storage (S3, GCS) or Render Disk and update `MODEL_PATH` in `app.py` accordingly.
- Avoid committing sensitive files (passwords, DB dumps).

If you want, I can initialize a Git repo and push this `FRONTEND` folder to GitHub for you.