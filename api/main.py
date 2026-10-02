from pathlib import Path
from time import perf_counter
import logging

import joblib
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# -------------------------
# Configuration
# -------------------------

MODEL_PATH = Path("model/qcm_decision_tree.joblib")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# -------------------------
# Chargement du modèle
# -------------------------

model = joblib.load(MODEL_PATH)


# -------------------------
# Application FastAPI
# -------------------------

app = FastAPI(
    title="QCM AI - E4",
    description="API d'analyse des résultats du QCM avec un modèle Decision Tree",
    version="1.0.0"
)


# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Modèle de données
# -------------------------

class PredictionRequest(BaseModel):

    score: float = Field(
        ge=0,
        le=100,
        description="Score obtenu au QCM"
    )

    temps_moyen: float = Field(
        ge=0,
        description="Temps moyen de réponse en secondes"
    )

    nb_erreurs: int = Field(
        ge=0,
        description="Nombre d'erreurs"
    )


class PredictionResponse(BaseModel):

    satisfait: int

    confidence: float


# -------------------------
# Routes
# -------------------------

@app.get("/")
def home():

    return {
        "application": "QCM AI",
        "version": "E4",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(data: PredictionRequest):

    start_time = perf_counter()

    features = pd.DataFrame([
        {
            "score": data.score,
            "temps_moyen": data.temps_moyen,
            "nb_erreurs": data.nb_erreurs
        }
    ])

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    confidence = float(max(probabilities))

    response_time = (
        perf_counter() - start_time
    ) * 1000

    logger.info(
        "Prediction=%s | Confidence=%.2f | ResponseTime=%.2f ms",
        prediction,
        confidence,
        response_time
    )

    return {
        "satisfait": int(prediction),
        "confidence": round(confidence, 3)
    }