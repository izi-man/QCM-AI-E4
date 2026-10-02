from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# Jeu de données de notre application QCM AI
data = {
    "score": [
        100, 90, 80, 70, 60,
        50, 40, 30, 20, 10,
        95, 85, 75, 65, 55,
        45, 35, 25, 15, 5
    ],

    "temps_moyen": [
        5, 7, 8, 10, 12,
        15, 18, 20, 22, 25,
        6, 9, 11, 13, 14,
        16, 19, 21, 23, 28
    ],

    "nb_erreurs": [
        0, 0, 1, 1, 2,
        2, 3, 3, 4, 5,
        0, 1, 1, 2, 2,
        3, 3, 4, 4, 5
    ],

    "satisfait": [
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0
    ]
}


df = pd.DataFrame(data)

# Variables utilisées par le modèle
X = df[
    [
        "score",
        "temps_moyen",
        "nb_erreurs"
    ]
]

# Variable à prédire
y = df["satisfait"]


# Séparation entraînement / test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Création du modèle
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)


# Entraînement
model.fit(X_train, y_train)


# Évaluation
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy : {accuracy:.2f}")
print()
print(classification_report(
    y_test,
    predictions
))


# Sauvegarde du modèle
Path("model").mkdir(
    exist_ok=True
)

joblib.dump(
    model,
    "model/qcm_decision_tree.joblib"
)

print()
print(
    "Modèle sauvegardé dans "
    "model/qcm_decision_tree.joblib"
)