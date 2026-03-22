from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import os

app = FastAPI(title="ML Model API")

with open("model.pkl", "rb") as f:
    model = joblib.load(f)

FEATURE_COLS = ["LotArea", "YearBuilt", "FirstFlrSF", "SecondFlrSF",
                "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
LOG_FILE = "logs/predictions.csv"
os.makedirs("logs", exist_ok=True)

class InputData(BaseModel):
    LotArea: int
    YearBuilt: int
    FirstFlrSF: int
    SecondFlrSF: int
    FullBath: int
    BedroomAbvGr: int
    TotRmsAbvGrd: int

@app.get("/")
def root():
    return {"status": "ok", "message": "Model API is running"}

@app.post("/predict")
def predict(data: InputData):
    features = pd.DataFrame([{
        "LotArea": data.LotArea,
        "YearBuilt": data.YearBuilt,
        "1stFlrSF": data.FirstFlrSF,
        "2ndFlrSF": data.SecondFlrSF,
        "FullBath": data.FullBath,
        "BedroomAbvGr": data.BedroomAbvGr,
        "TotRmsAbvGrd": data.TotRmsAbvGrd
    }])
    prediction = model.predict(features)
    predicted_price = round(float(prediction[0]), 2)

    # Log each prediction
    log_row = features.iloc[0].to_dict()
    log_row["predicted_price"] = predicted_price
    log_row["timestamp"] = datetime.utcnow().isoformat()
    
    df_log = pd.DataFrame([log_row])
    df_log.to_csv(LOG_FILE, mode="a", header=not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0, index=False)

    return {"predicted_price": predicted_price}

@app.get("/report", response_class=HTMLResponse)
def get_report():
    report_path = "reports/data_drift.html"
    if not os.path.exists(report_path):
        return HTMLResponse("<h2>No report yet. Run monitor.py first.</h2>")
    with open(report_path) as f:
        return HTMLResponse(f.read())
