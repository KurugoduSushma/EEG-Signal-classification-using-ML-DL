# 🧠 EEG Classification Frontend

A Flask-based web application for EEG signal classification that allows users to upload datasets, view model performance, and predict neurological disorders in real time.

---


## ▶️ Quick Start (Local Setup)

### 1. Create Virtual Environment

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# CMD
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
python app.py
```

App will run at:

```
http://127.0.0.1:5000/
```
---

## 📁 Important Folders

* `templates/` → HTML pages (Login, Register, Upload, Predict)
* `static/` → CSS, images, UI assets
* `uploads/` → User uploaded datasets
* `eeg_saved_models/` → Trained ML models
* `app.py` → Main Flask application

---

## 🤖 Model Integration

* Uses pre-trained models (Random Forest, etc.)
* Models loaded using `joblib`
* Preprocessing includes:

  * Scaling (StandardScaler)
  * Feature Selection (SelectKBest)
  * Encoding

---


## 🎯 Summary

This frontend acts as the interface layer connecting users with machine learning models, enabling seamless EEG data processing, visualization, and prediction through a web-based system.

---
