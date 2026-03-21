from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="ML Model API")

# Load model once at startup
with open("model.pkl", "rb") as f:
    model = joblib.load(f)

# Define your input schema — adjust fields to match your model's features
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # ... add all your features here

@app.get("/")
def root():
    return {"status": "ok", "message": "Model API is running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}

