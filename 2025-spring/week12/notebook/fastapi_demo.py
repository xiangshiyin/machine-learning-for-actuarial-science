from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

label_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


# Define the expected request format
class FeaturesInput(BaseModel):
    features: list[float]


@app.post("/predict")
def predict(data: FeaturesInput):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0]), "label": label_map[int(prediction[0])]}
