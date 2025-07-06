# -Iris-Species-Classifier
# 🌸 Iris Species Classifier (Random Forest + Streamlit)

This project is a simple yet effective web application that classifies Iris flower species using a **Random Forest Classifier** trained on the famous **Iris dataset**. The app is built with **Streamlit** and allows users to input flower measurements and receive predictions instantly.

---

## 📁 Folder Structure

iris_streamlit_app/
│
├── app.py # Streamlit application script
├── iris_model.pkl # Trained Random Forest model
├── venv/ # (optional) Virtual environment folder
└── README.md # Project documentation

---

## ⚙️ Features

- Predicts Iris species (`setosa`, `versicolor`, `virginica`)
- Visualizes feature importances using bar charts
- Calculates performance metrics: **Accuracy, Precision, Recall, F1-score**
- Interactive sliders for user inputs
- Lightweight and runs locally using Streamlit

---

## 📊 Tech Stack

- **Python**
- **Scikit-learn**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Streamlit**

---

## 🚀 How to Run the App

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/iris_streamlit_app.git
cd iris_streamlit_app

Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
