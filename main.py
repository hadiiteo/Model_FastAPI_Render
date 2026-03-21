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
    LotArea: int
    YearBuilt: int
    FirstFlrSF: int   # renamed — Python doesn't allow '1st' as variable name
    SecondFlrSF: int  # renamed — same reason
    FullBath: int
    BedroomAbvGr: int
    TotRmsAbvGrd: int

@app.get("/")
def root():
    return {"status": "ok", "message": "Model API is running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[
        data.LotArea,
        data.YearBuilt,
        data.FirstFlrSF,   # mapped back to correct order
        data.SecondFlrSF,
        data.FullBath,
        data.BedroomAbvGr,
        data.TotRmsAbvGrd
    ]])
    prediction = model.predict(features)
    return {"predicted_price": round(float(prediction[0]), 2)}

