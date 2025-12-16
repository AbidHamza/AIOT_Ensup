# Dossier mqtt-log/

## 📁 À propos de ce dossier

Ce dossier contient les **fichiers de logs** générés par le broker MQTT (Mosquitto) lors de son exécution.

## 🎯 Objectif pédagogique

### Qu'est-ce qu'un log MQTT ?

Un **log** est un journal d'événements qui enregistre toutes les activités du broker MQTT :
- Connexions et déconnexions des clients
- Messages publiés et reçus
- Erreurs et avertissements
- Informations de débogage

### Pourquoi c'est important ?

Les logs sont essentiels pour :
- **Déboguer** : Comprendre pourquoi une connexion échoue
- **Monitorer** : Surveiller l'activité du broker
- **Auditer** : Traçabilité des messages et connexions
- **Diagnostiquer** : Identifier les problèmes de performance ou sécurité

## 📚 Configuration des logs

Dans `mosquitto.conf`, on peut configurer :

```conf
# Activer les logs dans un fichier
log_dest file /mosquitto/log/mosquitto.log

# Types de logs à enregistrer
log_type error       # Erreurs critiques
log_type warning     # Avertissements
log_type notice      # Notifications importantes
log_type information # Informations générales
log_type all         # Tout (développement uniquement)
```

## 🔍 Types de logs

### 1. Logs d'erreur (error)

Exemples :
```
Error: Invalid protocol version
Error: Connection refused
Error: Bad username or password
```

### 2. Logs d'avertissement (warning)

Exemples :
```
Warning: Client disconnected unexpectedly
Warning: Topic filter exceeds maximum length
```

### 3. Logs de notification (notice)

Exemples :
```
New connection from 192.168.1.100
Client client123 disconnected
New client connected: client456
```

### 4. Logs d'information (information)

Exemples :
```
Sending CONNACK to client123
Received PUBLISH from client123 (d0, q0, r0, m0, 'sensors/temperature', ...)
Sending PUBACK to client123
```

## 📊 Format des logs

Format typique Mosquitto :
```
Timestamp [Type] Message details
```

Exemple réel :
```
1704067200: New connection from 172.18.0.1:52341 on port 1883.
1704067201: New client connected from 172.18.0.1:52341 as client123 (p2, c1, k60).
1704067202: Received PUBLISH from client123 (d0, q0, r0, m0, 'sensors/temp', ... (5 bytes))
1704067203: Sending PUBLISH to client456 (d0, q0, r0, m0, 'sensors/temp', ... (5 bytes))
1704067204: Client client123 disconnected.
```

### Explication des codes QoS dans les logs

Dans `(d0, q0, r0, m0, 'topic', ...)` :
- **d0/d1** : Duplicate flag (0=non dupliqué, 1=dupliqué)
- **q0/q1/q2** : QoS level (0, 1, ou 2)
- **r0/r1** : Retain flag (0=non retained, 1=retained)
- **m0/m1-m65535** : Message ID (0 pour QoS 0, ID unique pour QoS 1/2)

## 🔧 Utilisation pratique

### Visualiser les logs en temps réel

```bash
# Suivre les logs en direct (tail -f)
docker-compose logs -f mqtt-broker

# Ou directement le fichier
tail -f mqtt-log/mosquitto.log
```

### Filtrer les logs

```bash
# Voir seulement les erreurs
grep "Error" mqtt-log/mosquitto.log

# Voir les connexions
grep "New connection" mqtt-log/mosquitto.log

# Voir les messages publiés
grep "PUBLISH" mqtt-log/mosquitto.log
```

### Analyser les logs

```bash
# Compter les connexions
grep -c "New connection" mqtt-log/mosquitto.log

# Voir les dernières erreurs
grep "Error" mqtt-log/mosquitto.log | tail -20

# Statistiques par type
grep -c "PUBLISH" mqtt-log/mosquitto.log  # Nombre de messages
grep -c "disconnected" mqtt-log/mosquitto.log  # Déconnexions
```

## 🎓 Exercice pratique : Observer les logs

### Exercice 1 : Connexion simple

1. **Démarrer le broker :**
   ```bash
   docker-compose up -d mqtt-broker
   ```

2. **Se connecter avec un client :**
   ```python
   import paho.mqtt.client as mqtt
   client = mqtt.Client("test_client")
   client.connect("localhost", 1883)
   ```

3. **Observer les logs :**
   ```bash
   tail -f mqtt-log/mosquitto.log
   ```
   
   Vous devriez voir :
   ```
   New connection from 127.0.0.1:xxxxx
   New client connected as test_client
   ```

### Exercice 2 : Publier un message

1. **Publier un message :**
   ```python
   client.publish("sensors/temperature", "22.5")
   ```

2. **Observer dans les logs :**
   ```
   Received PUBLISH from test_client (d0, q0, r0, m0, 'sensors/temperature', ...)
   ```

### Exercice 3 : Analyser un problème

Simuler une erreur et observer :
1. Connexion avec mauvais mot de passe
2. Message sur topic trop long
3. Client qui se déconnecte brutalement

## 📖 Cas d'usage avancés

### Rotation des logs

En production, il faut limiter la taille des logs :

```conf
# Dans mosquitto.conf (si supporté)
log_timestamp true
log_timestamp_format %Y-%m-%d %H:%M:%S
```

Utiliser des outils externes comme `logrotate` pour gérer la rotation.

### Logs pour audit sécurité

Activer tous les logs pour traçabilité complète :
```conf
log_type all
```

⚠️ **Attention** : Produit beaucoup de données, utiliser avec modération.

### Monitoring avec logs

Intégrer les logs dans un système de monitoring :
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Grafana Loki**
- **Prometheus** (via exporter)

## 🛠️ Outils utiles

### Analyser les logs Python

```python
# Compter les connexions par client
with open('mqtt-log/mosquitto.log', 'r') as f:
    connections = [line for line in f if 'New client connected' in line]
    print(f"Total connections: {len(connections)}")
```

### Script bash pour statistiques

```bash
#!/bin/bash
LOG_FILE="mqtt-log/mosquitto.log"

echo "=== Statistiques MQTT ==="
echo "Connexions: $(grep -c "New connection" $LOG_FILE)"
echo "Messages publiés: $(grep -c "PUBLISH" $LOG_FILE)"
echo "Déconnexions: $(grep -c "disconnected" $LOG_FILE)"
echo "Erreurs: $(grep -c "Error" $LOG_FILE)"
```

## ⚠️ Bonnes pratiques

1. **En développement** : Logs détaillés pour déboguer
2. **En production** : Logs essentiels seulement (error, warning, notice)
3. **Rotation** : Limiter la taille des fichiers de logs
4. **Sécurité** : Les logs peuvent contenir des informations sensibles
5. **Stockage** : Les logs sont dans `.gitignore` (ne jamais committer)

## 📚 Pour aller plus loin

- **Room 7** : Observabilité et MLOps - Monitoring avancé
- **Documentation Mosquitto** : https://mosquitto.org/man/mosquitto-conf-5.html
- **Log Management** : Concepts de logging structuré

## 🎯 Résumé

- ✅ **mqtt-log/** : Journaux d'événements du broker
- ✅ **Essentiel pour** : Débogage, monitoring, audit
- ✅ **Configuration** : Via `mosquitto.conf`
- ✅ **Analyse** : Commandes `grep`, `tail`, scripts
- ✅ **Production** : Rotation et gestion de taille nécessaires

