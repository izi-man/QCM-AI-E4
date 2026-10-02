# Backlog Agile — QCM AI E4

## 1. Objectif du projet

Développer une application de QCM intégrant un service d'intelligence artificielle
capable d'analyser les résultats d'un utilisateur.

L'application permet de :
- répondre à 5 questions ;
- calculer le score ;
- mesurer le temps moyen de réponse ;
- comptabiliser les erreurs ;
- envoyer les résultats au modèle d'IA ;
- afficher une analyse et un niveau de confiance.

---

## 2. Backlog produit

| ID | Fonctionnalité | Priorité | Statut |
|---|---|---|---|
| US01 | Afficher les questions du QCM | Haute | Terminé |
| US02 | Permettre la sélection d'une réponse | Haute | Terminé |
| US03 | Calculer le score final | Haute | Terminé |
| US04 | Mesurer le temps de réponse | Moyenne | Terminé |
| US05 | Compter les erreurs | Moyenne | Terminé |
| US06 | Enregistrer les résultats pour l'analyse IA | Haute | Terminé |
| US07 | Prédire la satisfaction avec le modèle IA | Haute | Terminé |
| US08 | Afficher la confiance du modèle | Haute | Terminé |
| US09 | Exposer une API REST avec FastAPI | Haute | Terminé |
| US10 | Tester automatiquement l'API | Haute | Terminé |
| US11 | Automatiser les tests avec GitHub Actions | Haute | Terminé |
| US12 | Construire l'application avec Docker | Haute | Terminé |
| US13 | Vérifier l'état de santé de l'application | Haute | Terminé |
| US14 | Automatiser la vérification Docker dans la CI/CD | Haute | Terminé |

---

## 3. Organisation du travail

Le développement a été réalisé de manière itérative.

### Sprint 1 — Modèle IA

- définir les variables utilisées par le modèle ;
- préparer les données ;
- entraîner le Decision Tree ;
- évaluer le modèle ;
- sauvegarder le modèle au format Joblib.

### Sprint 2 — API et application

- développer l'API FastAPI ;
- créer l'endpoint `/predict` ;
- ajouter la validation des données ;
- développer l'interface QCM ;
- connecter le frontend à l'API ;
- afficher le résultat de l'analyse IA.

### Sprint 3 — Qualité et automatisation

- écrire les tests automatisés ;
- vérifier les cas nominaux ;
- vérifier les données invalides ;
- mettre en place GitHub Actions ;
- automatiser l'exécution de pytest.

### Sprint 4 — Conteneurisation et livraison

- créer le Dockerfile ;
- construire l'image Docker ;
- lancer le conteneur ;
- vérifier l'endpoint `/health` ;
- intégrer ces vérifications dans GitHub Actions.

---

## 4. Suivi technique

Chaque évolution importante est versionnée avec Git.

Le dépôt contient notamment :

- le code de l'API ;
- le frontend ;
- le modèle IA ;
- les tests ;
- le Dockerfile ;
- la configuration GitHub Actions ;
- la documentation.

Les tests sont exécutés automatiquement lors d'un push
sur la branche `master` ou `main`.

---

## 5. Definition of Done

Une fonctionnalité est considérée comme terminée lorsque :

- le code est développé ;
- les tests nécessaires sont présents ;
- les tests passent localement ;
- le code est versionné avec Git ;
- la CI est exécutée avec succès ;
- l'application peut être construite avec Docker lorsque nécessaire ;
- la fonctionnalité est documentée.

---

## 6. Outils utilisés

- Git / GitHub : gestion du code source et versioning
- GitHub Actions : intégration et automatisation
- Python : développement
- FastAPI : API REST
- Scikit-learn : modèle de Machine Learning
- Joblib : sauvegarde du modèle
- Pytest : tests automatisés
- Docker : conteneurisation