# AIoT Academy

> Formation complète et progressive pour devenir Architecte IA + IoT (AIoT)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Français](https://img.shields.io/badge/Language-Français-blue.svg)](README.md)

## 🎯 Objectif

Ce dépôt pédagogique vous accompagne dans l'apprentissage de l'architecture AIoT (Artificial Intelligence + Internet of Things) à travers une progression structurée en "rooms" (salles de formation). Chaque room contient des concepts théoriques, des exercices pratiques et des labs exécutables localement.

### Objectifs globaux

- Maîtriser la veille technologique, juridique et réglementaire dans le domaine IoT/AIoT
- Maîtriser les concepts fondamentaux de l'IoT (capteurs, protocoles, architectures)
- Comprendre et implémenter l'ingestion de données IoT (MQTT, HTTP)
- Concevoir et déployer des pipelines de données pour l'IoT
- Intégrer l'IA/ML dans les systèmes IoT (inférence, optimisation, drift)
- Sécuriser les systèmes AIoT (identité, secrets, OTA, conformité RGPD)
- Implémenter l'observabilité et le MLOps léger pour l'AIoT
- Réaliser un projet end-to-end complet

**Conforme au programme RNCP38920 - Expert des systèmes connectés (IoT)**

## 📚 Structure du dépôt

```
aiot-academy/
├── README.md                          # Ce fichier
├── CONTRIBUTING.md                    # Guide de contribution
├── docker-compose.yml                 # Services Docker (MQTT, DB, etc.)
│
├── room-0-veille-technologique/      # Veille technologique, juridique, réglementaire
├── room-1-foundations/                # Bases IoT : capteurs, simulateurs
├── room-2-iot-protocols-mqtt/        # Protocoles IoT : MQTT
├── room-3-data-ingestion-api/        # Ingestion de données : API HTTP
├── room-4-stream-processing-storage/ # Traitement stream et stockage
├── room-5-ml-inference/              # Inférence ML, latence, coûts
├── room-6-security-aiot/             # Sécurité AIoT (renforcé)
├── room-7-observability-mlops-lite/  # Observabilité et MLOps
├── room-8-capstone-end-to-end/       # Projet final end-to-end
│
└── SOLUTIONS/                         # Solutions détaillées (après essai)
```

## 🚀 Démarrage rapide

### Prérequis

- **Python 3.9+** (ou Node.js 18+ selon les rooms)
- **Docker** et **Docker Compose** (recommandé)
- **Git**
- Terminal : PowerShell (Windows) ou Terminal (Mac/Linux)

### Installation avec Docker (Recommandé)

1. **Cloner le dépôt**
   ```powershell
   # Windows PowerShell
   git clone <repository-url>
   cd aiot-academy
   ```

   ```bash
   # Mac/Linux Terminal
   git clone <repository-url>
   cd aiot-academy
   ```

2. **Démarrer les services de base**
   ```powershell
   # Windows PowerShell
   docker-compose up -d
   ```

   ```bash
   # Mac/Linux Terminal
   docker-compose up -d
   ```

3. **Vérifier que les services sont actifs**
   ```powershell
   # Windows PowerShell
   docker-compose ps
   ```

   ```bash
   # Mac/Linux Terminal
   docker-compose ps
   ```

### Installation sans Docker

Consultez le README de chaque room pour les instructions d'installation sans Docker.

## 📖 Roadmap de formation

| Room | Thème | Durée estimée | Prérequis |
|------|-------|---------------|-----------|
| [Room 0](room-0-veille-technologique/) | Veille technologique, juridique et réglementaire | 12h | Aucun |
| [Room 1](room-1-foundations/) | Fondations IoT | 4-6h | Room 0 (recommandé) |
| [Room 2](room-2-iot-protocols-mqtt/) | Protocoles IoT (MQTT) | 6-8h | Room 1 |
| [Room 3](room-3-data-ingestion-api/) | Ingestion de données (API) | 4-6h | Room 2 |
| [Room 4](room-4-stream-processing-storage/) | Traitement stream et stockage | 6-8h | Room 3 |
| [Room 5](room-5-ml-inference/) | Inférence ML | 6-8h | Room 4 |
| [Room 6](room-6-security-aiot/) | Sécurité AIoT (renforcé) | 12-16h | Room 5 |
| [Room 7](room-7-observability-mlops-lite/) | Observabilité et MLOps | 6-8h | Room 6 |
| [Room 8](room-8-capstone-end-to-end/) | Projet final end-to-end | 12-16h | Toutes les rooms |

**Durée totale estimée : 50-70 heures**

## 🏗️ Architecture AIoT de référence

```
┌─────────────────────────────────────────────────────────────┐
│                    AIoT Academy Architecture                │
└─────────────────────────────────────────────────────────────┘

[Devices/Simulateurs]  →  [Broker MQTT]  →  [Ingestion API]
       (Room 1)              (Room 2)          (Room 3)
                                                       ↓
                                           [Traitement Stream]
                                                   (Room 4)
                                                       ↓
                                           [Stockage] → [ML Inference]
                                                   (Room 5)
                                                       ↓
                                           [Sécurité + Observabilité]
                                                   (Rooms 6-7)
                                                       ↓
                                           [Dashboard/Actions]
                                                   (Room 8)
```

### Conventions techniques

- **Format de données** : JSON
- **Topics MQTT** : `aiot-academy/{device_id}/{sensor_type}/{data_type}`
- **Ports par défaut** :
  - MQTT Broker : `1883` (non sécurisé), `8883` (TLS)
  - API HTTP : `3000` (Node.js) ou `8000` (Python FastAPI)
  - PostgreSQL : `5432`
  - Redis : `6379`
  - Dashboard : `8080`

## 📚 Glossaire AIoT

| Terme | Définition |
|-------|------------|
| **AIoT** | Artificial Intelligence + Internet of Things. Intégration de l'IA dans les systèmes IoT. |
| **MQTT** | Message Queuing Telemetry Transport. Protocole de messagerie léger pour IoT. |
| **Broker** | Serveur MQTT qui reçoit et distribue les messages entre clients. |
| **Topic** | Canal de communication MQTT (ex: `sensors/temperature/room1`). |
| **Ingestion** | Processus de collecte et d'importation de données depuis les dispositifs IoT. |
| **Stream Processing** | Traitement de données en temps réel au fur et à mesure de leur arrivée. |
| **Inférence ML** | Utilisation d'un modèle ML entraîné pour faire des prédictions sur de nouvelles données. |
| **Drift** | Détérioration des performances d'un modèle ML due à des changements dans les données. |
| **OTA** | Over-The-Air. Mise à jour de firmware/logiciel à distance. |
| **Observabilité** | Capacité à comprendre l'état interne d'un système à partir de ses sorties externes. |
| **MLOps** | DevOps pour le Machine Learning. Automatisation du cycle de vie ML. |
| **RGPD** | Règlement Général sur la Protection des Données. Réglementation européenne sur la protection des données personnelles. |
| **mTLS** | Mutual TLS. Authentification mutuelle avec certificats (client et serveur s'authentifient). |
| **DPIA** | Data Protection Impact Assessment. Analyse d'impact sur la protection des données (obligatoire RGPD dans certains cas). |

## 🛠️ Technologies utilisées

### Par défaut (si non spécifié dans `/ressource`)

- **MQTT Broker** : Mosquitto (Docker)
- **Simulateurs capteurs** : Python (`paho-mqtt`) ou Node.js (`mqtt`)
- **Backend API** : Node.js (Express) ou Python (FastAPI)
- **Stockage** : SQLite (développement) ou PostgreSQL (production, Docker)
- **ML** : scikit-learn (modèles simples) + endpoint `/predict`
- **Tests** : scripts bash/PowerShell, curl, Postman

## ✅ Bonnes pratiques

1. **Sécurité** : Aucune clé réelle, secrets mockés, environnement local uniquement
2. **Sécurité renforcée** : Room 6 inclut une approche complète de la sécurité (authentification, chiffrement, RGPD, gestion des risques)
3. **Conformité** : Respect des réglementations (RGPD) et bonnes pratiques de sécurité (OWASP IoT Top 10, NIST)
4. **Éthique** : Exemples pédagogiques uniquement, pas de procédures nuisibles
5. **Progression** : Suivre les rooms dans l'ordre (commencer par Room 0 pour la veille)
6. **Pratique** : Faire tous les exercices avant de consulter les solutions
7. **Documentation** : Lire les README de chaque room avant de commencer
8. **Veille** : Mettre en place une veille technologique et réglementaire continue (Room 0)

## 🔒 Sécurité et Éthique

- ⚠️ **Tout se fait en environnement local** (Docker/localhost) avec données simulées
- ⚠️ **Aucune procédure nuisible** (intrusion, contournement, sabotage)
- ⚠️ **Pas de clés réelles** ou secrets en dur
- ⚠️ **Pas d'API payantes obligatoires** (mode mock/local fourni)
- ⚠️ **Exemples pédagogiques uniquement**

## 🐛 Dépannage

### Problèmes Docker

- **Port déjà utilisé** : Modifier les ports dans `docker-compose.yml`
- **Service ne démarre pas** : Vérifier les logs avec `docker-compose logs <service>`
- **Permissions Docker** : Vérifier que l'utilisateur est dans le groupe `docker` (Linux/Mac)

### Problèmes Python/Node.js

- **Module non trouvé** : Vérifier que l'environnement virtuel est activé (Python) ou que `node_modules` existe (Node.js)
- **Port déjà utilisé** : Changer le port dans le code ou tuer le processus qui utilise le port

### Problèmes MQTT

- **Connexion refusée** : Vérifier que Mosquitto est démarré (`docker-compose ps`)
- **Messages non reçus** : Vérifier les topics et QoS (Quality of Service)

## 🤝 Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines de contribution.

## 📄 Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

Ce dépôt pédagogique est inspiré par les meilleures pratiques de l'industrie pour l'AIoT.

## 📞 Support

Pour toute question ou problème :
1. Consulter les README de chaque room
2. Vérifier la section Dépannage ci-dessus
3. Ouvrir une issue sur le dépôt (si public)

---

**Bon apprentissage ! 🚀**

