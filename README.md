
# 🍷 Wine Quality Prediction ML

### An end-to-end machine learning project that predicts the **quality of wine** based on its chemical properties using Linear Regression, Flask, and a responsive CSS frontend.

---

## 🚀 Live Demo

Try it online: [Wine Quality Prediction ML](https://wine-quality-prediction-ml.onrender.com)

---

## 🛠 Technologies Used

* **Programming Language:** Python  
* **Machine Learning:** Scikit-learn (Linear Regression)  
* **Web Framework:** Flask  
* **Frontend:** HTML, CSS  
* **Deployment:** Render (Free hosting)  
* **Data:** Wine quality dataset (`winequality.csv`)  

---

## 💡 Features

* Predicts wine quality based on chemical attributes  
* Clean and responsive web interface  
* Hosted online for real-time usage  
* Uses a trained Linear Regression model for accurate predictions  
* Easy-to-use input form and result display  

---

## 📂 Project Structure

```

Wine-Quality-Prediction-ML/
├── app.py 📝 Flask backend
├── wine_quality_model.pkl 📦 Trained Linear Regression model
├── requirements.txt 📄 Python dependencies
├── templates/ 📁 HTML templates
│   ├── index.html 🖥️ Input form
│   └── result.html 🖥️ Prediction result
├── static/ 📁 Static assets
│   └── style.css 🎨 CSS styling
└── WineQT.csv 📊 Sample dataset

````

---

## ⚡ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/Wine-Quality-Prediction-ML.git
````

### 2️⃣ Navigate into the project folder

```bash
cd Wine-Quality-Prediction-ML
```

### 3️⃣ Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Flask application

```bash
python app.py
```

### 6️⃣ Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters wine features (e.g., acidity, sugar, pH, alcohol, etc.)
2. Flask loads the trained Linear Regression model
3. Input data is processed and passed to the model
4. The model predicts the **Wine Quality Score**
5. Result is displayed on the webpage

---

## 🚀 Future Improvements

* Add more ML algorithms for better accuracy
* Include confidence scores or probability ranges for predictions
* Enhance frontend with interactive charts and graphs
* Store historical predictions for analysis

---

## 📫 Contact

* **GitHub:** [https://github.com/PavanSurisetti](https://github.com/PavanSurisetti)
* **LinkedIn:** [https://www.linkedin.com/in/pavan-surisetti-b3281228b/](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## 📄 License

This project is licensed under the **MIT License**.
