import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, RegressionPreset

# Load reference (training) data
reference = pd.read_csv("reference_data.csv")

# Load current (production) logs
current = pd.read_csv("logs/predictions.csv")

# Drop timestamp before analysis
current_clean = current.drop(columns=["timestamp"], errors="ignore")

# --- Data Drift Report ---
drift_report = Report(metrics=[DataDriftPreset()])
drift_report.run(reference_data=reference, current_data=current_clean)
drift_report.save_html("reports/data_drift.html")
print("✅ Drift report saved to reports/data_drift.html")

# --- Regression Performance (if you have actuals) ---
# Uncomment if you ever collect ground truth sale prices
# perf_report = Report(metrics=[RegressionPreset()])
# perf_report.run(reference_data=reference, current_data=current_with_actuals)
# perf_report.save_html("reports/performance.html")
