import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# App UI
st.title("🌸 Iris Flower Species Predictor")
st.write("Input flower measurements to predict the species.")

# Inputs
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)[0]
probs = model.predict_proba(input_data)[0]

species = ['Setosa', 'Versicolor', 'Virginica']

# Output
st.subheader("🔍 Prediction:")
st.write(f"🌼 Predicted species: **{species[prediction]}**")

# Visualize prediction probabilities
st.subheader("📊 Prediction Probabilities:")
fig, ax = plt.subplots()
ax.bar(species, probs, color='lightgreen')
ax.set_ylabel("Probability")
ax.set_ylim([0, 1])
st.pyplot(fig)
