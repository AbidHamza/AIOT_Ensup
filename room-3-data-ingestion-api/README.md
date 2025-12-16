# Room 3 : Ingestion de données - API HTTP

> Création d'API REST pour l'ingestion de données IoT

## 📋 Objectifs pédagogiques

À la fin de cette room, vous serez capable de :

- Créer une API REST pour recevoir des données IoT
- Valider les données reçues
- Stocker les données dans une base de données
- Gérer les erreurs et la résilience
- Implémenter l'authentification basique (dev uniquement)

## 🎯 Durée estimée

4-6 heures

## 📚 Concepts abordés

1. **API REST pour IoT**
   - Endpoints pour l'ingestion
   - Format JSON des requêtes
   - Codes de statut HTTP

2. **Validation des données**
   - Schémas de validation (JSON Schema, Pydantic)
   - Gestion des erreurs de validation

3. **Stockage des données**
   - Connexion à PostgreSQL
   - Modèles de données
   - Transactions

4. **Architecture**
   - Séparation des couches (API, Service, Repository)
   - Gestion des erreurs centralisée

## 🛠️ Prérequis

- Rooms 1 et 2 terminées
- Docker et Docker Compose
- Python 3.9+ (FastAPI) ou Node.js 18+ (Express)

## 🚀 Installation

### Démarrer les services

```powershell
# Windows PowerShell
docker-compose up -d postgres
```

```bash
# Mac/Linux Terminal
docker-compose up -d postgres
```

### Installer les dépendances

```powershell
# Windows PowerShell
cd room-3-data-ingestion-api/src
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 📁 Structure de la room

```
room-3-data-ingestion-api/
├── README.md
├── src/
│   ├── main.py              # FastAPI app principale
│   ├── models.py            # Modèles de données
│   ├── database.py          # Configuration DB
│   └── requirements.txt
└── tests/
    └── test_api.py
```

## 🏃 Lab 1 : API d'ingestion basique

Créer un endpoint `/api/v1/sensors/data` qui accepte des données de capteurs.

## ➡️ Suite

Une fois cette room terminée, passez à [Room 4 : Traitement stream et stockage](../room-4-stream-processing-storage/).

