import streamlit as st
import pickle
import pandas as pd
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

# # Sample DataFrame (Can be replaced with real data)
# df = pd.DataFrame(
#     {
#         "Sepal Length": [5.1, 4.9, 6.2, 5.8],
#         "Sepal Width": [3.5, 3.0, 2.9, 2.7],
#         "Petal Length": [1.4, 1.4, 4.3, 5.1],
#         "Petal Width": [0.2, 0.2, 1.3, 1.9],
#         "Class": ["Setosa", "Setosa", "Versicolor", "Virginica"],
#     }
# )

# st.subheader("Sample Iris Dataset")
# st.dataframe(df)  # Display the DataFrame interactively
