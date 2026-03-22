from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse, HTMLResponse
import joblib
import numpy as np
import pandas as pd
import subprocess
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
    if not os.path.exists(LOG_FILE):
        return HTMLResponse("<h2>No predictions logged yet. Hit /predict first.</h2>")
    
    if not os.path.exists(REFERENCE_FILE):
        return HTMLResponse("<h2>No reference data found. Add reference_data.csv to the repo.</h2>")

    reference = pd.read_csv(REFERENCE_FILE)
    current = pd.read_csv(LOG_FILE).drop(columns=["timestamp"], errors="ignore")

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)

    return HTMLResponse(report.get_html())

@app.get("/download-logs")
def download_logs():
    if not os.path.exists(LOG_FILE):
        return {"error": "No logs yet"}
    return FileResponse(LOG_FILE, filename="predictions.csv")

@app.get("/logs-status")
def logs_status():
    return {
        "logs_folder_exists": os.path.exists("logs"),
        "predictions_csv_exists": os.path.exists(LOG_FILE),
        "file_size_bytes": os.path.getsize(LOG_FILE) if os.path.exists(LOG_FILE) else 0
    }

@app.post("/run-monitor")
def run_monitor():
    if not os.path.exists(LOG_FILE):
        return {"error": "No prediction logs yet"}
    try:
        subprocess.run(["python", "monitor.py"], check=True)
        return {"status": "Report generated. Visit /report to view."}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
