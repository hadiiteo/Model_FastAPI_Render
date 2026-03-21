# 🏠 Iowa Housing Price Predictor

A beginner machine learning project based on Kaggle's **Intro to Machine Learning** course. The model is trained on the Iowa Housing dataset, served via **FastAPI**, and deployed as a live web service on **Render**.

🔗 **Live API:** [https://model-fastapi-render.onrender.com/docs](https://model-fastapi-render.onrender.com/docs)  
📓 **Kaggle Notebook:** [exercise-your-first-machine-learning-model](https://www.kaggle.com/code/haditeo/exercise-your-first-machine-learning-model/)

---

## 📖 About

This project demonstrates an end-to-end ML workflow — from training a simple regression model in Kaggle, to deploying it as a REST API accessible over the internet. It is intended as a portfolio starting point for ML model deployment using free-tier tools.

> 💡 Claude AI was used to help design and integrate the overall project structure, from model export to API deployment.

---

## 🏗️ Solution Architecture

<p align="center">
<svg width="680" viewBox="0 0 680 590" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#888780" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- ── LANE BACKGROUNDS ── -->
  <rect x="20" y="40" width="300" height="200" rx="12" fill="none" stroke="#B4B2A9" stroke-width="1" stroke-dasharray="6 4"/>
  <text font-family="sans-serif" font-size="12" x="36" y="62" fill="#888780">Training (Kaggle)</text>

  <rect x="20" y="270" width="300" height="270" rx="12" fill="none" stroke="#B4B2A9" stroke-width="1" stroke-dasharray="6 4"/>
  <text font-family="sans-serif" font-size="12" x="36" y="292" fill="#888780">Deployment</text>

  <rect x="358" y="40" width="302" height="430" rx="12" fill="none" stroke="#B4B2A9" stroke-width="1" stroke-dasharray="6 4"/>
  <text font-family="sans-serif" font-size="12" x="374" y="62" fill="#888780">Runtime</text>

  <!-- ── TRAINING LANE ── -->

  <!-- Iowa Housing CSV -->
  <rect x="44" y="80" width="130" height="52" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="109" y="101" text-anchor="middle" dominant-baseline="central" fill="#085041">Iowa Housing</text>
  <text font-family="sans-serif" font-size="11" x="109" y="119" text-anchor="middle" dominant-baseline="central" fill="#0F6E56">CSV data source</text>

  <!-- Kaggle Notebook -->
  <rect x="196" y="80" width="104" height="52" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="248" y="101" text-anchor="middle" dominant-baseline="central" fill="#085041">Notebook</text>
  <text font-family="sans-serif" font-size="11" x="248" y="119" text-anchor="middle" dominant-baseline="central" fill="#0F6E56">pandas + sklearn</text>

  <!-- Arrow: CSV → Notebook -->
  <line x1="174" y1="106" x2="194" y2="106" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- model.pkl -->
  <rect x="90" y="168" width="140" height="52" rx="8" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="160" y="189" text-anchor="middle" dominant-baseline="central" fill="#412402">model.pkl</text>
  <text font-family="sans-serif" font-size="11" x="160" y="207" text-anchor="middle" dominant-baseline="central" fill="#854F0B">joblib export</text>

  <!-- Arrow: Notebook → model.pkl -->
  <path d="M248 132 L248 152 L160 152 L160 168" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ── DEPLOYMENT LANE ── -->

  <!-- GitHub -->
  <rect x="44" y="308" width="120" height="52" rx="8" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="104" y="329" text-anchor="middle" dominant-baseline="central" fill="#2C2C2A">GitHub</text>
  <text font-family="sans-serif" font-size="11" x="104" y="347" text-anchor="middle" dominant-baseline="central" fill="#5F5E5A">main.py + model.pkl</text>

  <!-- FastAPI -->
  <rect x="196" y="308" width="104" height="52" rx="8" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="248" y="329" text-anchor="middle" dominant-baseline="central" fill="#26215C">FastAPI</text>
  <text font-family="sans-serif" font-size="11" x="248" y="347" text-anchor="middle" dominant-baseline="central" fill="#534AB7">POST /predict</text>

  <!-- Arrow: GitHub → FastAPI -->
  <line x1="164" y1="334" x2="194" y2="334" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Docker -->
  <rect x="90" y="396" width="140" height="52" rx="8" fill="#FAECE7" stroke="#993C1D" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="160" y="417" text-anchor="middle" dominant-baseline="central" fill="#4A1B0C">Docker</text>
  <text font-family="sans-serif" font-size="11" x="160" y="435" text-anchor="middle" dominant-baseline="central" fill="#993C1D">Containerised app</text>

  <!-- Arrow: FastAPI → Docker -->
  <path d="M248 360 L248 380 L160 380 L160 396" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Render -->
  <rect x="90" y="464" width="140" height="52" rx="8" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="160" y="485" text-anchor="middle" dominant-baseline="central" fill="#26215C">Render</text>
  <text font-family="sans-serif" font-size="11" x="160" y="503" text-anchor="middle" dominant-baseline="central" fill="#534AB7">Free web service</text>

  <!-- Arrow: Docker → Render -->
  <line x1="160" y1="448" x2="160" y2="464" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ── CROSS-LANE: model.pkl → GitHub ── -->
  <path d="M160 220 L160 250 L104 250 L104 308" fill="none" stroke="#888780" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#arrow)"/>
  <text font-family="sans-serif" font-size="11" x="128" y="246" text-anchor="middle" fill="#888780">commit</text>

  <!-- ── CROSS-LANE: Render → Runtime ── -->
  <line x1="300" y1="490" x2="378" y2="422" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ── RUNTIME LANE ── -->

  <!-- Live API Endpoint -->
  <rect x="378" y="80" width="252" height="52" rx="8" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="504" y="101" text-anchor="middle" dominant-baseline="central" fill="#26215C">Live API endpoint</text>
  <text font-family="sans-serif" font-size="10" x="504" y="119" text-anchor="middle" dominant-baseline="central" fill="#534AB7">model-fastapi-render.onrender.com</text>

  <!-- Render → API vertical -->
  <path d="M504 422 L504 380 L504 132" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Client / User -->
  <rect x="430" y="180" width="148" height="52" rx="8" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="504" y="201" text-anchor="middle" dominant-baseline="central" fill="#042C53">Client / User</text>
  <text font-family="sans-serif" font-size="11" x="504" y="219" text-anchor="middle" dominant-baseline="central" fill="#185FA5">JSON request body</text>

  <!-- Arrow: API → Client -->
  <line x1="504" y1="132" x2="504" y2="180" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Prediction Response -->
  <rect x="378" y="280" width="252" height="52" rx="8" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="504" y="301" text-anchor="middle" dominant-baseline="central" fill="#042C53">Prediction response</text>
  <text font-family="sans-serif" font-size="11" x="504" y="319" text-anchor="middle" dominant-baseline="central" fill="#185FA5">{ "predicted_price": ... }</text>

  <!-- Arrow: Client → Response -->
  <line x1="504" y1="232" x2="504" y2="280" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Swagger UI -->
  <rect x="378" y="380" width="252" height="52" rx="8" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="13" font-weight="500" x="504" y="401" text-anchor="middle" dominant-baseline="central" fill="#042C53">Swagger UI /docs</text>
  <text font-family="sans-serif" font-size="11" x="504" y="419" text-anchor="middle" dominant-baseline="central" fill="#185FA5">Interactive testing</text>

  <!-- Arrow: Response → Swagger -->
  <line x1="504" y1="332" x2="504" y2="380" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ── NEXT IMPROVEMENTS ── -->
  <rect x="378" y="455" width="120" height="38" rx="8" fill="none" stroke="#B4B2A9" stroke-width="1" stroke-dasharray="5 3"/>
  <text font-family="sans-serif" font-size="11" x="438" y="478" text-anchor="middle" fill="#888780">CI/CD (GitHub)</text>

  <rect x="510" y="455" width="140" height="38" rx="8" fill="none" stroke="#B4B2A9" stroke-width="1" stroke-dasharray="5 3"/>
  <text font-family="sans-serif" font-size="11" x="580" y="478" text-anchor="middle" fill="#888780">Evidently AI</text>

  <text font-family="sans-serif" font-size="10" x="504" y="506" text-anchor="middle" fill="#B4B2A9">Next improvements</text>
</svg>
</p>

---

## 🧠 Model

- **Type:** Decision Tree Regressor (scikit-learn)
- **Dataset:** Iowa Housing (Kaggle Intro to Machine Learning)
- **Target:** Predicted house sale price (USD)
- **Export format:** `.pkl` via `joblib`

### Input Features

| Field | Type | Description |
|---|---|---|
| `LotArea` | `int` | Lot size in square feet |
| `YearBuilt` | `int` | Year the house was built |
| `FirstFlrSF` | `int` | First floor area in square feet |
| `SecondFlrSF` | `int` | Second floor area in square feet |
| `FullBath` | `int` | Number of full bathrooms |
| `BedroomAbvGr` | `int` | Number of bedrooms above ground |
| `TotRmsAbvGrd` | `int` | Total rooms above ground |

---

## 🚀 Tech Stack

| Layer | Tool |
|---|---|
| Model Training | Python, scikit-learn, pandas (Kaggle) |
| Model Export | `joblib` → `.pkl` |
| API Framework | FastAPI |
| Containerisation | Docker |
| Deployment | Render (free tier, GitHub integration) |
| Source Control | GitHub |

---

## 🔧 Running Locally

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn main:app --reload
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive Swagger UI.

**Or run with Docker:**

```bash
docker build -t housing-predictor .
docker run -p 8000:8000 housing-predictor
```

---

## 📬 API Usage

**Endpoint:** `POST /predict`

**Request body (JSON):**
```json
{
  "LotArea": 8450,
  "YearBuilt": 2003,
  "FirstFlrSF": 856,
  "SecondFlrSF": 854,
  "FullBath": 2,
  "BedroomAbvGr": 3,
  "TotRmsAbvGrd": 8
}
```

**Response:**
```json
{
  "predicted_price": 208500.0
}
```

---

## 📁 Project Structure

```
├── main.py              # FastAPI app and prediction endpoint
├── model.pkl            # Trained scikit-learn model (exported via joblib)
├── Dockerfile           # Container definition for the API
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 💡 Key Lessons Learned

- A **CSV file** is required as the data source to train the model
- The trained model is exported as a **`.pkl` file** using `joblib` for deployment
- **FastAPI** is used to expose the model as a REST API endpoint
- **Docker** packages the FastAPI app and model into a portable container, ensuring consistent behaviour across environments
- **Render** provides a free hosting service with direct **GitHub integration**, making deployment straightforward — any push to the main branch triggers a redeploy
- The entire pipeline (train → export → containerise → serve → deploy) can be assembled using free tools

---

## 🔭 Next Improvements

- [ ] **GitHub CI/CD** — automate testing and deployment on every push
- [ ] **Evidently AI integration** — monitor model performance and detect data drift over time

---

## 📚 Learning Reference

- [Kaggle — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Render Deployment Guide](https://render.com/docs)
- [Evidently AI](https://www.evidentlyai.com/)

---

## 👤 Author

**Hadi** — Production Support Engineer transitioning into AI/MLOps  
[LinkedIn](https://linkedin.com/in/haditeo/) · [Kaggle](https://www.kaggle.com/haditeo)
