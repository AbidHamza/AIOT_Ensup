# Structure complète du dépôt AIoT Academy

## 📁 Arborescence complète

```
aiot-academy/
│
├── README.md                          # Documentation principale
├── CONTRIBUTING.md                    # Guide de contribution
├── ARCHITECTURE.md                    # Architecture détaillée
├── STRUCTURE.md                       # Ce fichier (arborescence)
├── docker-compose.yml                 # Services Docker (MQTT, DB, etc.)
├── .gitignore                         # Fichiers à ignorer par Git
│
├── mqtt-config/                       # Configuration Mosquitto
│   └── mosquitto.conf
├── mqtt-data/                         # Données MQTT (généré)
├── mqtt-log/                          # Logs MQTT (généré)
│
├── room-0-veille-technologique/       # Room 0: Veille technologique, juridique, réglementaire
│   ├── README.md
│   └── src/
│       ├── veille_setup_guide.md      # Guide pratique de mise en place de la veille
│       └── rgpd_iot_checklist.md      # Checklist RGPD pour solutions IoT
│
├── room-1-foundations/                # Room 1: Bases IoT
│   ├── README.md
│   ├── src/
│   │   ├── temperature_sensor.py
│   │   └── requirements.txt
│   └── troubleshooting.md
│
├── room-2-iot-protocols-mqtt/        # Room 2: Protocoles IoT MQTT
│   ├── README.md
│   └── src/
│       ├── mqtt_publisher.py
│       ├── mqtt_subscriber.py
│       └── requirements.txt
│
├── room-3-data-ingestion-api/        # Room 3: Ingestion de données API
│   └── README.md
│
├── room-4-stream-processing-storage/ # Room 4: Traitement stream et stockage
│   └── README.md
│
├── room-5-ml-inference/              # Room 5: Inférence ML
│   └── README.md
│
├── room-6-security-aiot/             # Room 6: Sécurité AIoT (renforcé)
│   ├── README.md                      # Contenu étendu avec sécurité complète
│   └── src/
│       └── security_checklist.md      # Checklist de sécurité complète
│
├── room-7-observability-mlops-lite/  # Room 7: Observabilité et MLOps
│   └── README.md
│
├── room-8-capstone-end-to-end/       # Room 8: Projet final end-to-end
│   └── README.md
│
└── SOLUTIONS/                         # Solutions détaillées (après essai)
    └── README.md
```

## 📊 Conformité avec le programme RNCP38920

### Bloc de compétences 1 : Réaliser une étude d'opportunité (100h)

- ✅ **Module 1 - Veille technologique** → Room 0
- ✅ **Module 2 - Collecte et analyse des besoins** → Intégré dans Room 0 et Room 8
- ✅ **Module 3 - Contexte et stratégie** → Room 0
- ✅ **Module 4 - Note de cadrage** → Room 0 et Room 8
- ✅ **Module 5 - Benchmark solutions** → Room 0
- ✅ **Module 6 - Solutions éco-responsables** → Intégré dans plusieurs rooms
- ✅ **Module 7 - Cartographie systèmes** → Room 4
- ✅ **Module 8 - Analyse des risques** → Room 6 (renforcé)
- ✅ **Module 9 - Impacts environnementaux** → Intégré dans plusieurs rooms
- ✅ **Module 10 - Étude de faisabilité** → Room 8

### Bloc de compétences 2 : Concevoir une solution AIoT (144h)

- ✅ **Module 1 - Cartographie fonctionnelle** → Room 4, Room 8
- ✅ **Module 2 - Modélisation architecture technique** → Room 2, Room 4, Room 8
- ✅ **Module 3 - Gouvernance et cartographie données** → Room 0 (RGPD), Room 4
- ✅ **Module 4 - Modélisation architecture IA** → Room 5
- ✅ **Module 5 - Conception modèles IA** → Room 5
- ✅ **Module 6 - Architecture données pour IA** → Room 5
- ✅ **Module 7 - Maquettage infrastructure** → Room 8
- ✅ **Module 8 - Paramétrage plateforme** → Room 2, Room 3, Room 4
- ✅ **Module 9 - Tests de validation** → Room 8
- ✅ **Module 10 - Tests d'échange données** → Room 2, Room 3

### Bloc de compétences 3 : Intégrer et maintenir (60h)

- ✅ **Module 1 - Processus et maintenabilité** → Room 7, Room 8
- ✅ **Module 2 - Documentation technique** → Toutes les rooms
- ✅ **Module 3 - Mise en production** → Room 8
- ✅ **Module 4 - Expertise technique** → Rooms 1-8
- ✅ **Module 5 - Accompagnement changement** → Room 8
- ✅ **Module 6 - Gestion impacts et formation** → Room 8

### Bloc de compétences 4 : Piloter un projet agile (65h)

- ✅ **Module 1 - Conception cahiers des charges** → Room 8
- ✅ **Module 2 - Gestion projet agile** → Room 8
- ✅ **Module 3 - Suivi et pilotage** → Room 7, Room 8
- ✅ **Module 4 - Gestion prestataires** → Room 8
- ✅ **Module 5 - Gestion d'équipe agile** → Room 8
- ✅ **Module 6 - Inclusion et handicap** → Intégré dans l'approche
- ✅ **Module 7 - Communication interpersonnelle** → Intégré dans l'approche
- ✅ **Module 8 - Innovation et gestion conflits** → Intégré dans l'approche
- ✅ **Module 9 - Communication inclusive** → Intégré dans l'approche
- ✅ **Module 10 - Animation réunions à distance** → Intégré dans l'approche
- ✅ **Module 11 - Partage information télétravail** → Intégré dans l'approche

## 🔒 Renforcements sécurité

### Room 6 - Sécurité AIoT (renforcé)

**Contenu ajouté/renforcé** :

1. **Identification et analyse des risques**
   - Risques sécurité des données
   - Risques réseaux
   - Risques conformité réglementaire
   - Cartographie des risques

2. **Sécurité des communications**
   - TLS/SSL pour MQTT (détaillé)
   - HTTPS pour API
   - Chiffrement des données (transit et repos)
   - VPN et tunnels sécurisés

3. **Authentification et autorisation**
   - Certificats X.509 (génération, rotation, révocation)
   - JWT pour API
   - ACL MQTT
   - Authentification mutuelle (mTLS)

4. **Gestion des secrets**
   - Variables d'environnement
   - Secrets managers (Vault local)
   - Rotation des clés
   - Stockage sécurisé

5. **Sécurité des données et RGPD**
   - Chiffrement au repos
   - Anonymisation/pseudonymisation
   - Gestion des accès (IAM)
   - Conformité RGPD

6. **Mises à jour OTA sécurisées**
   - Stratégies de déploiement
   - Vérification d'intégrité (signature)
   - Rollback

7. **Security by Design**
   - Threat modeling
   - Hardening
   - Tests de sécurité

8. **Gestion des incidents et conformité**
   - Détection et réponse
   - Conformité réglementaire (ISO 27001, IEC 62443, RGPD)
   - Audit et reporting

**Ressources ajoutées** :
- Checklist de sécurité complète (`security_checklist.md`)
- Labs pratiques détaillés
- Exercices d'analyse de risques

### Room 0 - Veille technologique

**Contenu sécurité intégré** :
- Veille réglementaire (RGPD, ePrivacy)
- Checklist RGPD pour solutions IoT
- Analyse des risques juridiques
- Conformité réglementaire

## 📈 Progression recommandée

1. **Room 0** : Veille technologique (12h) - Fondations théoriques
2. **Room 1** : Fondations IoT (4-6h) - Pratique de base
3. **Room 2** : Protocoles MQTT (6-8h) - Communication
4. **Room 3** : Ingestion API (4-6h) - Collecte de données
5. **Room 4** : Stream processing (6-8h) - Traitement
6. **Room 5** : Inférence ML (6-8h) - Intelligence
7. **Room 6** : Sécurité AIoT (12-16h) - Sécurisation complète
8. **Room 7** : Observabilité (6-8h) - Monitoring
9. **Room 8** : Projet final (12-16h) - Intégration complète

**Note** : Cette formation est conçue pour être complétée à votre propre rythme. Prenez le temps nécessaire pour bien comprendre chaque concept.
