import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Iris Flower Classifier")

# Create a two-column layout
col1, col2 = st.columns([1, 1])  # Adjust ratio if needed

# Left column: Prediction Panel
with col1:
    st.subheader("Enter Features for Prediction")
    sepal_length = st.number_input("Sepal Length", value=5.1)
    sepal_width = st.number_input("Sepal Width", value=3.5)
    petal_length = st.number_input("Petal Length", value=1.4)
    petal_width = st.number_input("Petal Width", value=0.2)

    if st.button("Predict"):
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)[0]
        st.success(f"**Predicted Class:** {prediction}")

# Right column: DataFrame Display
with col2:
    st.subheader("Sample Iris Dataset")
    df = pd.DataFrame(
        {
            "Sepal Length": [5.1, 4.9, 6.2, 5.8],
            "Sepal Width": [3.5, 3.0, 2.9, 2.7],
            "Petal Length": [1.4, 1.4, 4.3, 5.1],
            "Petal Width": [0.2, 0.2, 1.3, 1.9],
            "Class": ["Setosa", "Setosa", "Versicolor", "Virginica"],
        }
    )
    st.dataframe(df)  # Interactive table
