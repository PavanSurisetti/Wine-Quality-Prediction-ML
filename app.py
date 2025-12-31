from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('wine_quality_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load dataset for column names
data = pd.read_csv('WineQT.csv')
col_names = data.columns[:11]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values from form
        features = [float(request.form[col]) for col in col_names]
        features_array = np.array(features).reshape(1, -1)

        # Scale features
        features_scaled = scaler.transform(features_array)

        # Make prediction
        prediction = model.predict(features_scaled)[0]

        return render_template('result.html', prediction_text=f'Predicted Wine Quality: {prediction:.2f}')
    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
