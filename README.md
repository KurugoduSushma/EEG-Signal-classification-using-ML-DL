# 🧠 EEG Signal Classification System for Neurological Disorders

## 📌 Project Overview

This project presents an intelligent web-based system designed to classify neurological disorders using EEG (Electroencephalogram) signals. By leveraging advanced Machine Learning and Deep Learning techniques, the system analyzes brain activity patterns and predicts disorders with high accuracy.

The application provides an end-to-end solution—from dataset upload and preprocessing to model prediction and result visualization—through an interactive user interface.

---

## 🚀 Key Features

* 🔐 User Authentication (Register/Login)
* 📂 EEG Dataset Upload (.csv)
* 📊 Dataset Preview & Analysis
* 🤖 Model Training & Accuracy Comparison
* 🧠 Real-time Prediction of Disorders
* 📈 Confusion Matrix & Performance Metrics
* 🌐 Web-based Interactive Interface

---

## 🧠 Disorders Detected

The system classifies EEG signals into multiple neurological conditions such as:

* Addictive Disorder
* Anxiety Disorder
* Obsessive-Compulsive Disorder (OCD)
* Schizophrenia
* Trauma-related Disorders
* Mood Disorders
* Normal Brain Activity

---

## 🛠️ Technologies Used

### 💻 Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### ⚙️ Backend

* Python
* Flask Framework


### 📊 Data Processing

* Pandas
* NumPy
* Seaborn
* Matplotlib

### Database

* MySQL

 ### 🗄️ Database Setup (Using XAMPP)

This project uses XAMPP (Apache + MySQL) to manage the database connection between the frontend (Flask app) and backend logic.

🔧 Steps to Configure XAMPP

* Install and open XAMPP Control Panel
* Start:
    * ✅ Apache
    * ✅ MySQL
  
Open phpMyAdmin
👉 http://localhost/phpmyadmin

### 🔧 Tools & Libraries

* Joblib (Model Saving/Loading)
* SMOTE (Handling Imbalanced Data)
* Label Encoding & Feature Scaling

---

## 🤖 Algorithms Used

* Random Forest (Primary Model - High Accuracy ~99%)
* XGBoost
* Artificial Neural Network (ANN)

---

## 🔄 System Workflow

1. User registers and logs into the system
2. Upload EEG dataset (CSV format)
3. Data preprocessing (cleaning, encoding, scaling)
4. Feature selection using SelectKBest
5. Model training using ML algorithms
6. Performance evaluation (accuracy, confusion matrix)
7. User inputs new EEG data
8. System predicts neurological disorder

---

## 📊 Model Performance

| Model         | Accuracy |
| ------------- | -------- |
| Random Forest | 0.99     |
| XGBoost       | 0.98     |
| ANN           | 0.90     |

---

## 🧪 Data Preprocessing Steps

* Handling missing values using median
* Label encoding for categorical data
* Feature scaling using StandardScaler
* Feature selection using SelectKBest
* Class balancing using SMOTE

---

## 📁 Project Structure

```
EEG-Classification/
│
├── BACKEND/
│   ├── code.ipynb              # Model training & preprocessing
│   ├── EEG_dataset.csv        # Original EEG dataset
│
├── FRONTEND/
│   ├── templates/             # HTML pages (login, register, upload, predict)
│   ├── static/                # CSS, images, UI assets
│   ├── uploads/               # Uploaded CSV files
│   ├── eeg_saved_models/      # Saved ML models & preprocessors
│   ├── app.py                 # Flask backend server
│   ├── db.sql                 # MySQL database schema
│   ├── app.db                 # Local database (if used)
│   ├── requirements.txt       # Python dependencies
│   ├── rf_model.pkl           # Trained Random Forest model
│   ├── README.md              # Frontend documentation
│
├── .venv/                     # Virtual environment (ignored in GitHub)
├── README.md                  # Main project documentation
├── .gitignore
```

---

## ⚠️ Challenges Faced

* Handling missing and noisy EEG data
* Class imbalance in dataset
* Model compatibility issues (version mismatch)
* Integration of ML model with web application

---

## 🔮 Future Enhancements

* Real-time EEG signal integration
* Multimodal data (wearables, medical history)
* Explainable AI (XAI) for better interpretability
* Cloud deployment & scalability
* Transformer-based deep learning models

---



## 🎯 Conclusion

This EEG classification system demonstrates how machine learning can transform neurological diagnosis by enabling faster, more accurate, and automated predictions. It enhances clinical decision-making and reduces manual analysis efforts, paving the way for smarter healthcare solutions.

---

## 👩‍💻 Author

Developed as part of a research-based project on EEG Signal Classification using Machine Learning and Deep Learning techniques.

---
