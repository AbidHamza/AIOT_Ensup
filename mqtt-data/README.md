# Dossier mqtt-data/

## 📁 À propos de ce dossier

Ce dossier contient les **données persistantes** générées par le broker MQTT (Mosquitto) lors de son exécution.

## 🎯 Objectif pédagogique

### Qu'est-ce que la persistance MQTT ?

Dans MQTT, la **persistance** permet au broker de :
- Sauvegarder les messages avec QoS 1 ou 2 qui n'ont pas été encore complètement délivrés
- Conserver les abonnements des clients (subscriptions) même après redémarrage
- Maintenir l'état des sessions des clients (clean session = false)

### Quand est-ce utilisé ?

Le dossier `mqtt-data/` est utilisé uniquement si la **persistence est activée** dans la configuration Mosquitto (`mosquitto.conf`).

**Configuration typique :**
```conf
persistence true
persistence_location /mosquitto/data/
```

## 📚 Concepts clés

### 1. Messages avec QoS > 0

Les messages avec **QoS 1 ou 2** sont stockés ici jusqu'à leur confirmation de réception :

- **QoS 1** : Au moins une fois (duplication possible)
  - Le message est stocké jusqu'à réception du PUBACK
  
- **QoS 2** : Exactement une fois (garantie d'unicité)
  - Le message est stocké jusqu'à complétion de l'échange complet (PUBREC, PUBREL, PUBCOMP)

### 2. Sessions persistantes (Clean Session = false)

Quand un client se connecte avec `clean_session = false`, le broker :
- Conserve les messages QoS 1/2 non délivrés pour ce client
- Mémorise les abonnements (topics) du client
- Restaure l'état après reconnexion

### 3. Retained Messages

Les messages **retained** (retenus) sont stockés ici pour être envoyés automatiquement aux nouveaux abonnés.

## 🔍 Contenu du dossier

**Note** : Ce dossier est généralement vide au début et se remplit automatiquement lors de l'utilisation du broker.

Fichiers typiques générés :
- `mosquitto.db` : Base de données SQLite contenant les messages en attente
- Autres fichiers temporaires du broker

## ⚙️ En pratique

### Vérifier le contenu

```bash
# Lister les fichiers générés
ls -la mqtt-data/

# Voir la taille du dossier
du -sh mqtt-data/
```

### Effacer les données

⚠️ **Attention** : Effacer ce dossier supprime :
- Les messages en attente de délivrance
- Les sessions persistantes
- Les messages retained

**Pour réinitialiser (développement uniquement) :**
```bash
# Arrêter le broker d'abord
docker-compose down

# Supprimer les données
rm -rf mqtt-data/*

# Redémarrer
docker-compose up -d
```

## 🎓 Exercice pratique

Pour observer la persistance en action :

1. **Publier un message avec QoS 1 à un client non connecté :**
   ```python
   # Le message sera stocké dans mqtt-data/
   client.publish("test/topic", "message", qos=1)
   ```

2. **Vérifier que le fichier est créé :**
   ```bash
   ls -la mqtt-data/
   ```

3. **Le client se connecte et reçoit le message :**
   - Le message est retiré de la persistance après délivrance

## 📖 Pour aller plus loin

- **Documentation Mosquitto** : https://mosquitto.org/man/mosquitto-conf-5.html
- **QoS Levels** : Voir Room 2 - Protocoles IoT MQTT
- **Clean Session** : Concept expliqué dans Room 2

## ⚠️ Important

- Ce dossier est **dans .gitignore** (ne jamais committer des données de production)
- En développement, on peut le nettoyer régulièrement
- En production, attention à la croissance de taille (surveiller l'espace disque)

