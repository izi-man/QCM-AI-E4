import joblib
import pandas as pd
from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)

model = joblib.load(
    "model/qcm_decision_tree.joblib"
)


# =========================
# TEST HEALTH
# =========================

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"

    assert data["model_loaded"] is True


# =========================
# TEST PAGE PRINCIPALE
# =========================

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "QCM AI"

    assert data["version"] == "E4"

    assert data["status"] == "running"


# =========================
# TEST PREDICTION
# =========================

def test_predict():

    response = client.post(
        "/predict",
        json={
            "score": 80,
            "temps_moyen": 10,
            "nb_erreurs": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "satisfait" in data

    assert "confidence" in data

    assert data["satisfait"] in [0, 1]

    assert 0 <= data["confidence"] <= 1


# =========================
# TEST SCORE TROP ELEVE
# =========================

def test_invalid_score_high():

    response = client.post(
        "/predict",
        json={
            "score": 150,
            "temps_moyen": 10,
            "nb_erreurs": 1
        }
    )

    assert response.status_code == 422


# =========================
# TEST SCORE NEGATIF
# =========================

def test_invalid_score_negative():

    response = client.post(
        "/predict",
        json={
            "score": -10,
            "temps_moyen": 10,
            "nb_erreurs": 1
        }
    )

    assert response.status_code == 422


# =========================
# TEST TEMPS NEGATIF
# =========================

def test_invalid_time():

    response = client.post(
        "/predict",
        json={
            "score": 80,
            "temps_moyen": -5,
            "nb_erreurs": 1
        }
    )

    assert response.status_code == 422


# =========================
# TEST ERREURS NEGATIVES
# =========================

def test_invalid_errors():

    response = client.post(
        "/predict",
        json={
            "score": 80,
            "temps_moyen": 10,
            "nb_erreurs": -1
        }
    )

    assert response.status_code == 422


# =========================
# TEST MODELE
# =========================

def test_model_prediction():

    data = pd.DataFrame([{
        "score": 80,
        "temps_moyen": 10,
        "nb_erreurs": 1
    }])

    prediction = model.predict(data)

    assert len(prediction) == 1

    assert prediction[0] in [0, 1]

# =========================
# TEST PROBABILITE MODELE
# =========================

def test_model_probability():

    data = pd.DataFrame([{
        "score": 80,
        "temps_moyen": 10,
        "nb_erreurs": 1
    }])

    probabilities = model.predict_proba(data)[0]

    assert len(probabilities) == 2

    assert all(
        0 <= probability <= 1
        for probability in probabilities
    )

    assert abs(
        sum(probabilities) - 1
    ) < 0.001