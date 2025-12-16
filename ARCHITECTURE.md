# Architecture AIoT Academy

## 📐 Schéma logique

```
┌─────────────────────────────────────────────────────────────────┐
│                    AIoT Academy - Architecture                  │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐
│  Simulateurs │  Room 1: Fondations
│   Capteurs   │  - TemperatureSensor
│   IoT        │  - HumiditySensor
│              │  - PressureSensor
└──────┬───────┘
       │
       │ MQTT (QoS 1)
       ▼
┌──────────────┐
│   Broker     │  Room 2: Protocoles MQTT
│    MQTT      │  - Topics: aiot-academy/{device}/{sensor}/{type}
│ (Mosquitto)  │  - Wildcards: +, #
└──────┬───────┘
       │
       ├──────────────────┬──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Publisher  │  │  Subscriber  │  │ Stream Proc. │
│   (Devices)  │  │  (Gateway)   │  │   (Room 4)   │
└──────────────┘  └──────────────┘  └──────┬───────┘
                                            │
                                            ▼
                                    ┌──────────────┐
                                    │   Ingestion  │  Room 3: API Ingestion
                                    │     API      │  - POST /api/v1/sensors/data
                                    │  (FastAPI)   │  - Validation (Pydantic)
                                    └──────┬───────┘
                                           │
                                           ▼
                                    ┌──────────────┐
                                    │  PostgreSQL  │  Room 4: Stockage
                                    │   InfluxDB   │  - Time-series DB
                                    │  (Timescale) │  - Optimisé temporel
                                    └──────┬───────┘
                                           │
                                           ▼
                                    ┌──────────────┐
                                    │   ML Model   │  Room 5: ML Inference
                                    │  Inference   │  - Prédiction
                                    │   Service    │  - Anomaly Detection
                                    └──────┬───────┘
                                           │
                                           ▼
                                    ┌──────────────┐
                                    │  Security    │  Room 6: Sécurité
                                    │   Layer      │  - TLS/SSL
                                    │              │  - Authentication
                                    └──────┬───────┘
                                           │
                                           ▼
                                    ┌──────────────┐
                                    │ Observability│  Room 7: Monitoring
                                    │   Grafana    │  - Dashboards
                                    │   Metrics    │  - Logs
                                    └──────────────┘
```

## 🔄 Flux de données

### Flux principal

1. **Collection** (Room 1)
   - Simulateurs génèrent des données de capteurs
   - Format: JSON avec `sensor_id`, `value`, `timestamp`

2. **Transport** (Room 2)
   - Publication MQTT sur topics structurés
   - QoS 1 pour garantie de livraison

3. **Ingestion** (Room 3)
   - API REST reçoit les données
   - Validation et normalisation
   - Stockage initial

4. **Traitement** (Room 4)
   - Stream processing (filtrage, agrégation)
   - Stockage optimisé (time-series DB)

5. **Intelligence** (Room 5)
   - Inférence ML pour prédictions
   - Détection d'anomalies
   - Alertes automatiques

6. **Sécurité** (Room 6)
   - Chiffrement en transit (TLS)
   - Authentification des devices
   - Gestion des secrets

7. **Observabilité** (Room 7)
   - Logging structuré
   - Métriques temps réel
   - Dashboards Grafana

## 📊 Formats de données

### Message MQTT (Room 2)

```json
{
  "sensor_id": "TEMP-001",
  "temperature": 22.3,
  "timestamp": "2025-01-XXT10:30:45.123Z",
  "unit": "celsius"
}
```

### Requête API (Room 3)

```json
POST /api/v1/sensors/data
{
  "device_id": "DEVICE-001",
  "sensor_type": "temperature",
  "value": 22.3,
  "timestamp": "2025-01-XXT10:30:45.123Z",
  "metadata": {
    "location": "room-101",
    "calibration_date": "2025-01-01"
  }
}
```

### Réponse API

```json
{
  "status": "success",
  "message_id": "msg-12345",
  "timestamp": "2025-01-XXT10:30:46.000Z"
}
```

## 🔐 Architecture de sécurité (Room 6)

```
┌──────────────┐
│   Devices    │───(X.509 Cert)──►┌──────────────┐
│  IoT (TLS)   │                  │   Broker     │
└──────────────┘                  │  MQTT (TLS)  │
                                  └──────┬───────┘
                                         │
                                         │ (HTTPS)
                                         ▼
                                  ┌──────────────┐
                                  │   API REST   │
                                  │  (JWT Auth)  │
                                  └──────────────┘
```

## 📈 Métriques et Monitoring (Room 7)

- **Métriques système** : CPU, RAM, réseau
- **Métriques applicatives** : Latence API, throughput MQTT
- **Métriques ML** : Accuracy, latency inference, drift
- **Métriques IoT** : Nombre de messages, devices connectés

## 🔌 Ports et services

| Service | Port | Protocole | Description |
|---------|------|-----------|-------------|
| MQTT Broker | 1883 | MQTT | Port non sécurisé (dev) |
| MQTT Broker TLS | 8883 | MQTTS | Port sécurisé |
| MQTT WebSocket | 9001 | WS | WebSocket |
| API HTTP | 3000/8000 | HTTP | API REST |
| PostgreSQL | 5432 | TCP | Base de données |
| Redis | 6379 | TCP | Cache/Queue |
| Grafana | 3000 | HTTP | Dashboards |
| InfluxDB | 8086 | HTTP | Time-series DB |

## 🏗️ Stack technique

- **Broker MQTT** : Eclipse Mosquitto
- **API** : FastAPI (Python) ou Express (Node.js)
- **Base de données** : PostgreSQL + TimescaleDB (extension)
- **Time-series** : InfluxDB (optionnel)
- **Cache/Queue** : Redis
- **ML** : scikit-learn (Python)
- **Monitoring** : Grafana + Prometheus (optionnel)
- **Containerisation** : Docker + Docker Compose

## 🔄 Patterns utilisés

1. **Pub/Sub** : MQTT pour communication découplée
2. **API Gateway** : Point d'entrée unique pour l'ingestion
3. **Event Sourcing** : Historique complet des événements IoT
4. **CQRS léger** : Séparation lecture/écriture (optionnel)
5. **Microservices** : Services indépendants par fonctionnalité

## 📝 Notes d'architecture

- **Scalabilité** : Architecture horizontale possible
- **Résilience** : Retry, circuit breakers (avancé)
- **Performance** : Cache Redis, batch processing
- **Maintenabilité** : Code modulaire, tests unitaires

---

Pour plus de détails, consultez les README de chaque room.

