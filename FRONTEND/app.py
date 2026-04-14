
from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from werkzeug.utils import secure_filename
import logging


# Set main logging level
logging.basicConfig(level=logging.INFO)

# Reduce matplotlib logs
logging.getLogger('matplotlib').setLevel(logging.WARNING)

# Reduce werkzeug logs (optional)
logging.getLogger('werkzeug').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


app = Flask(__name__)
app.secret_key = 'eeg_secret_key_2025'

# MySQL configurations (read from environment)
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME', 'eeg_users')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Paths
MODEL_PATH = 'eeg_saved_models/'
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Random Forest model and preprocessing objects
try:
    rf_model = joblib.load(os.path.join(MODEL_PATH, 'rf_model.pkl'))
    scaler = joblib.load(os.path.join(MODEL_PATH, 'scaler.pkl'))
    selector = joblib.load(os.path.join(MODEL_PATH, 'selector.pkl'))
    le_sex = joblib.load(os.path.join(MODEL_PATH, 'sex_encoder.pkl'))
    le_target = joblib.load(os.path.join(MODEL_PATH, 'target_encoder.pkl'))
    selected_features = joblib.load(os.path.join(MODEL_PATH, 'selected_features.pkl'))
    all_features = joblib.load(os.path.join(MODEL_PATH, 'all_features.pkl'))
except FileNotFoundError as e:
    logger.error(f"Error loading model or preprocessing objects: {str(e)}")
    raise

# Preprocessing function for single sample
def preprocess_single_sample(input_data, selected_features, scaler, selector, le_sex, all_features):
    try:
        # Create DataFrame with user inputs for selected features
        df = pd.DataFrame([input_data], columns=selected_features)
        # Encode 'sex' if present
        if 'sex' in df.columns:
            try:
                df['sex'] = le_sex.transform([df['sex'].iloc[0]])[0]
            except ValueError:
                logger.error("Invalid value for 'sex'. Expected 'M' or 'F'.")
                raise ValueError("Invalid value for 'sex'. Please select Male or Female.")
        # Fill missing numeric values with median
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        # Create a full feature DataFrame matching training data
        full_df = pd.DataFrame(0.0, index=[0], columns=all_features)
        for feature in selected_features:
            if feature in full_df.columns:
                full_df[feature] = df[feature]
        # Scale and select features
        X_scaled = scaler.transform(full_df)
        X_selected = selector.transform(X_scaled)
        logger.debug(f"Preprocessed single sample shape: {X_selected.shape}")
        return X_selected
    except Exception as e:
        logger.error(f"Preprocessing error: {str(e)}")
        raise

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                          (username, email, password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError as e:
            flash('Registration failed: email already registered', 'danger')
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, email, password FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user and user[3] == password:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password', 'danger')
        except Exception as e:
            flash(f'Login failed: {str(e)}', 'danger')
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'danger')
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/about')
def about():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'danger')
        return redirect(url_for('login'))
    return render_template('about.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            try:
                df = pd.read_csv(filepath, index_col=None)
                # Drop problematic columns
                df.drop(columns=['no.', 'eeg.date', 'Unnamed: 122'], errors='ignore', inplace=True)
                data_html = df.head().to_html(classes='table table-striped')
                session['uploaded_file'] = filepath
                flash('File uploaded successfully!', 'success')
                return render_template('upload.html', data_html=data_html)
            except Exception as e:
                flash(f'Error processing file: {str(e)}', 'danger')
        else:
            flash('Please upload a CSV file', 'danger')
    return render_template('upload.html')

@app.route('/algo')
def algo():
    accuracies = {
        'Random Forest': 0.99,
        'XGBoost': 0.98,
        'ANN': 0.90
        
    }
    return render_template('algo.html', accuracies=accuracies)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect('predict')
        
        df = pd.read_csv('uploads/final_dataset.csv')
        x = df.drop('main.disorder', axis=1)
        y = df['main.disorder']
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
        rf_model1 = RandomForestClassifier()
        rf_model1.fit(x_train, y_train)
        data = pd.read_csv(file)
        prediction = rf_model1.predict(data)

        if prediction == 0:
            predicts = "Prediction of EEG Signal Classification is Addictive disorder"
        elif prediction == 1: 
            predicts = "Prediction of EEG Signal Classification is Anxiety disorder"
        elif prediction == 2: 
            predicts = "Prediction of EEG Signal Classification is Healthy control"
        elif prediction == 3: 
            predicts = "Prediction of EEG Signal Classification is Mood disorder"
        elif prediction == 4: 
            predicts = "Prediction of EEG Signal Classification is Obsessive compulsive disorder"
        elif prediction == 5: 
            predicts = "Prediction of EEG Signal Classification is Schizophrenia"
        elif prediction == 6: 
            predicts = "Prediction of EEG Signal Classification is Trauma and stress related disorder"

        y_pred = rf_model1.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred) 

        # Calculate accuracy score on the test set
        y_pred = rf_model1.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        
        # Create confusion matrix plot
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')
        cm_image_path = 'static/cm_plot.png'  # Save the plot image path
        plt.savefig(cm_image_path)
        plt.close()

        return render_template('predict.html', predicts=predicts, accuracy=accuracy, 
                               cm_image_path=cm_image_path, 
                               algorithm="RandomForestClassifier")
        

    return render_template('predict.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('uploaded_file', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)