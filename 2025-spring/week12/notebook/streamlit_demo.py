import streamlit as st
import pickle
import numpy as np

# Load model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Iris Flower Classifier")

# User input
sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.write(f"Predicted Class: {prediction}")
