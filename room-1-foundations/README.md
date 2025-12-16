# Room 1 : Fondations IoT

> Bases de l'IoT : capteurs, simulateurs, concepts fondamentaux

## 📋 Objectifs pédagogiques

À la fin de cette room, vous serez capable de :

- Comprendre les concepts fondamentaux de l'IoT
- Simuler des capteurs IoT (température, humidité, pression, etc.)
- Générer des données de capteurs réalistes
- Visualiser les données capteurs en temps réel
- Comprendre l'architecture d'un système IoT simple

## 🎯 Durée estimée

4-6 heures

## 📚 Concepts abordés

1. **Introduction à l'IoT**
   - Qu'est-ce que l'IoT ?
   - Composants d'un système IoT (capteurs, actionneurs, gateway, cloud)
   - Cas d'usage IoT

2. **Capteurs IoT**
   - Types de capteurs (température, humidité, pression, accéléromètre, etc.)
   - Caractéristiques des capteurs (résolution, précision, plage de mesure)
   - Format de données capteurs

3. **Simulation de capteurs**
   - Pourquoi simuler ? (coût, développement, tests)
   - Modèles de données réalistes
   - Génération de séries temporelles

## 🛠️ Prérequis

- Python 3.9+ installé
- pip installé
- (Optionnel) Docker et Docker Compose

## 🚀 Installation

### Avec Docker

```powershell
# Windows PowerShell
docker-compose up -d
```

```bash
# Mac/Linux Terminal
docker-compose up -d
```

### Sans Docker

```powershell
# Windows PowerShell
cd room-1-foundations/src
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Mac/Linux Terminal
cd room-1-foundations/src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📁 Structure de la room

```
room-1-foundations/
├── README.md                    # Ce fichier
├── scenarios/                   # Scénarios pédagogiques
│   ├── scenario-1-temperature.md
│   └── scenario-2-multi-sensors.md
├── exercises/                   # Exercices guidés
│   ├── exercise-1-basic-sensor.md
│   └── exercise-2-sensor-array.md
├── checklists/                  # Checklists de validation
│   └── room-1-checklist.md
├── src/                         # Code source
│   ├── sensor_simulator.py
│   ├── temperature_sensor.py
│   └── requirements.txt
├── tests/                       # Tests
│   └── test_sensors.py
└── troubleshooting.md           # Dépannage
```

## 🏃 Lab 1 : Simulateur de capteur de température

### Objectif

Créer un simulateur simple qui génère des données de température réalistes.

### Code de base

Voir `src/temperature_sensor.py` pour le code complet.

### Exécution

```powershell
# Windows PowerShell
cd src
python temperature_sensor.py
```

```bash
# Mac/Linux Terminal
cd src
python3 temperature_sensor.py
```

### Résultat attendu

```
Sensor ID: TEMP-001
Temperature: 22.3°C
Timestamp: 2025-01-XX 10:30:45
```

## 📊 Lab 2 : Visualisation en temps réel

### Objectif

Visualiser les données de plusieurs capteurs en temps réel avec matplotlib.

### Exécution

```powershell
# Windows PowerShell
python src/visualizer.py
```

```bash
# Mac/Linux Terminal
python3 src/visualizer.py
```

## ✅ Checklist de validation

- [ ] J'ai compris les concepts fondamentaux de l'IoT
- [ ] Je peux simuler un capteur de température
- [ ] Je peux générer des données réalistes pour plusieurs capteurs
- [ ] Je peux visualiser les données en temps réel
- [ ] J'ai complété tous les exercices

## 🐛 Dépannage

Voir [troubleshooting.md](troubleshooting.md) pour les erreurs fréquentes.

## 📖 Ressources supplémentaires

- [IoT Fundamentals](https://www.iotforall.com/what-is-iot)
- [Sensor Types](https://www.electronicsforu.com/technology-trends/iot-sensors-types)

## ➡️ Suite

Une fois cette room terminée, passez à [Room 2 : Protocoles IoT (MQTT)](../room-2-iot-protocols-mqtt/).

