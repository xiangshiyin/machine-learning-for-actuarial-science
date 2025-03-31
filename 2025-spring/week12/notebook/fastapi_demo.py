from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)


# Define the expected request format
class FeaturesInput(BaseModel):
    features: list[float]


@app.post("/predict")
def predict(data: FeaturesInput):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
