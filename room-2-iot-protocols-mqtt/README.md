# Room 2 : Protocoles IoT - MQTT

> Communication IoT avec MQTT : publish, subscribe, topics, QoS

## Objectifs pédagogiques

À la fin de cette room, vous serez capable de :

- Comprendre le protocole MQTT et ses concepts clés
- Publier des données depuis un capteur vers un broker MQTT
- S'abonner à des topics MQTT pour recevoir des données
- Gérer les niveaux de QoS (Quality of Service)
- Utiliser des patterns de topics MQTT (wildcards, multi-level)
- Comprendre la rétention de messages et les last will testament

## À propos de cette room

Cette room vous apprend à utiliser MQTT, le protocole de communication le plus utilisé dans l'IoT. Prenez le temps nécessaire pour bien maîtriser chaque concept avant de passer au suivant.

## Concepts abordés

1. **MQTT : Introduction**
   - Qu'est-ce que MQTT ?
   - Architecture MQTT (Publisher, Subscriber, Broker)
   - Avantages de MQTT pour l'IoT

2. **Topics et Messages**
   - Structure des topics (`aiot-academy/device/sensor/type`)
   - Wildcards (`+`, `#`)
   - Format des messages (JSON recommandé)

3. **Quality of Service (QoS)**
   - QoS 0 : At most once
   - QoS 1 : At least once
   - QoS 2 : Exactly once

4. **Fonctionnalités avancées**
   - Retained messages
   - Last Will and Testament (LWT)
   - Clean session vs persistent session

## Prérequis

- Room 1 terminée
- Docker et Docker Compose (pour le broker)
- Python 3.9+ ou Node.js 18+

## Installation

### Démarrer le broker MQTT (Mosquitto)

```powershell
# Windows PowerShell
docker-compose up -d mqtt-broker
# Vérifier que le service est actif
docker-compose ps mqtt-broker
```

```bash
# Mac/Linux Terminal
docker-compose up -d mqtt-broker
docker-compose ps mqtt-broker
```

### Installer les dépendances Python

```powershell
# Windows PowerShell
cd room-2-iot-protocols-mqtt/src
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Mac/Linux Terminal
cd room-2-iot-protocols-mqtt/src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Structure de la room

```
room-2-iot-protocols-mqtt/
├── README.md
├── scenarios/
│   ├── scenario-1-basic-pub-sub.md
│   └── scenario-2-multiple-devices.md
├── exercises/
│   ├── exercise-1-publish-temperature.md
│   └── exercise-2-subscribe-multiple-topics.md
├── src/
│   ├── mqtt_publisher.py      # Publisher simple
│   ├── mqtt_subscriber.py     # Subscriber simple
│   ├── sensor_publisher.py    # Publisher de capteurs
│   └── requirements.txt
└── troubleshooting.md
```

## Lab 1 : Publisher MQTT simple

### Objectif

Publier des messages sur un topic MQTT depuis un simulateur de capteur. Ce lab vous apprend à :
- Connecter un client MQTT à un broker
- Publier des messages sur un topic
- Structurer les messages en JSON

### Comprendre MQTT

MQTT (Message Queuing Telemetry Transport) est un protocole de messagerie léger conçu pour l'IoT. Il fonctionne selon un modèle publish/subscribe :

- **Publisher** : Envoie des messages sur un topic
- **Subscriber** : Reçoit les messages d'un topic
- **Broker** : Serveur qui distribue les messages entre publishers et subscribers
- **Topic** : Canal de communication (ex: `sensors/temperature/room1`)

### Code de base

Le fichier `src/mqtt_publisher.py` contient le code complet. Avant de l'exécuter, lisez-le pour comprendre ce qu'il fait.

### Exécution

Vous devez ouvrir deux terminaux pour ce lab :

**Terminal 1 : Subscriber (pour voir les messages reçus)**

```powershell
# Windows PowerShell
cd room-2-iot-protocols-mqtt/src
python mqtt_subscriber.py
```

```bash
# Mac/Linux Terminal
cd room-2-iot-protocols-mqtt/src
python3 mqtt_subscriber.py
```

**Terminal 2 : Publisher (pour envoyer les messages)**

```powershell
# Windows PowerShell
cd room-2-iot-protocols-mqtt/src
python mqtt_publisher.py
```

```bash
# Mac/Linux Terminal
cd room-2-iot-protocols-mqtt/src
python3 mqtt_publisher.py
```

**Important** : Démarrez d'abord le subscriber, puis le publisher. Le subscriber doit être prêt à recevoir les messages avant que le publisher ne commence à envoyer.

### Résultat attendu

Dans le terminal du subscriber, vous devriez voir :

```
Message reçu sur topic: aiot-academy/TEMP-001/temperature
Données: {"sensor_id": "TEMP-001", "temperature": 22.3, "timestamp": "2025-01-15T10:30:45"}
```

Dans le terminal du publisher, vous devriez voir :

```
Message publié sur topic: aiot-academy/TEMP-001/temperature
Température: 22.3°C
```

### Analyse du résultat

- **Topic** : `aiot-academy/TEMP-001/temperature` suit la convention `{organisation}/{device_id}/{sensor_type}`
- **Format JSON** : Les données sont structurées en JSON pour faciliter leur traitement
- **Timestamp** : Chaque message contient un timestamp pour savoir quand la mesure a été prise

### Exercice pratique

Modifiez le code pour :
1. Changer le topic (ex: `maison/salon/temperature`)
2. Ajouter d'autres données au message (ex: humidité, pression)
3. Modifier la fréquence de publication (ex: toutes les 5 secondes)

## Lab 2 : Subscriber avec wildcards

### Objectif

S'abonner à plusieurs topics en utilisant des wildcards MQTT.

### Exemple de wildcard

```python
# S'abonner à tous les capteurs de température
client.subscribe("aiot-academy/+/temperature")

# S'abonner à tous les topics d'un device
client.subscribe("aiot-academy/TEMP-001/#")
```

## Lab 3 : Publisher de capteurs multiples

### Objectif

Publier les données de plusieurs capteurs (température, humidité, pression) simultanément.

## Checklist de validation

Avant de passer à la Room 3, assurez-vous d'avoir complété :

- [ ] Je comprends le fonctionnement de MQTT (publisher, subscriber, broker, topic)
- [ ] Je peux publier des messages sur un topic
- [ ] Je peux m'abonner à un topic et recevoir des messages
- [ ] Je comprends les différents niveaux de QoS (0, 1, 2)
- [ ] Je peux utiliser des wildcards (`+`, `#`) pour m'abonner à plusieurs topics
- [ ] J'ai complété tous les exercices pratiques
- [ ] J'ai documenté mon travail dans un README.md

**Note** : Si vous n'avez pas complété tous les éléments, ce n'est pas grave. Vous pouvez toujours passer à la suite et revenir plus tard si nécessaire.

## Comment soumettre votre travail

Voir la section "Comment soumettre votre travail" dans le [README principal](../../README.md#comment-soumettre-votre-travail) pour les instructions détaillées.

**Rappel** : Créez un dossier `votre-nom-room-2/` avec votre code, vos exercices et un README.md expliquant ce que vous avez fait.

## Dépannage

### Broker MQTT non accessible

**Erreur :** `Connection refused` ou `Connection timed out`

**Solution :**
```powershell
# Vérifier que Mosquitto est démarré
docker-compose ps mqtt-broker

# Redémarrer si nécessaire
docker-compose restart mqtt-broker

# Vérifier les logs
docker-compose logs mqtt-broker
```

### Messages non reçus

**Vérifications :**
1. Le topic est-il correct ? (sensible à la casse)
2. Le QoS correspond-il entre publisher et subscriber ?
3. Le subscriber est-il connecté avant la publication ?

## Ressources supplémentaires

- [MQTT.org](https://mqtt.org/)
- [Eclipse Mosquitto Documentation](https://mosquitto.org/documentation/)

## Suite

Une fois cette room terminée, passez à [Room 3 : Ingestion de données (API)](../room-3-data-ingestion-api/).

