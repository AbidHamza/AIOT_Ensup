# AIoT Academy

> Formation complète et progressive pour devenir Architecte IA + IoT (AIoT)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Français](https://img.shields.io/badge/Language-Français-blue.svg)](README.md)

## Table des matières

- [Objectif](#objectif)
- [Comment utiliser cette formation](#comment-utiliser-cette-formation)
- [Structure du dépôt](#structure-du-dépôt)
- [Démarrage rapide](#démarrage-rapide)
- [Roadmap de formation](#roadmap-de-formation)
- [Architecture AIoT de référence](#architecture-aiot-de-référence)
- [Glossaire technique](#glossaire-technique)
- [Technologies utilisées](#technologies-utilisées)
- [Bonnes pratiques d'apprentissage](#bonnes-pratiques-dapprentissage)
- [Sécurité et Éthique](#sécurité-et-éthique)
- [Dépannage](#dépannage)
- [Comment soumettre votre travail](#comment-soumettre-votre-travail)
- [Contribution](#contribution)
- [Support](#support)

**Astuce** : Consultez le [Guide de navigation](GUIDE-NAVIGATION.md) pour une aide visuelle à la navigation dans le dépôt.

## Objectif

Ce dépôt pédagogique vous accompagne dans l'apprentissage de l'architecture AIoT (Artificial Intelligence + Internet of Things) à travers une progression structurée en "rooms" (salles de formation). Chaque room contient des concepts théoriques, des exercices pratiques et des labs exécutables localement.

### Approche pédagogique

Cette formation suit une approche progressive et pratique :

1. **Théorie appliquée** : Chaque concept est expliqué avec des exemples concrets et des cas d'usage réels
2. **Pratique immédiate** : Des exercices guidés vous permettent de mettre en pratique immédiatement les concepts appris
3. **Progression structurée** : Les rooms s'appuient les unes sur les autres pour construire progressivement vos compétences
4. **Autonomie** : Des explications détaillées vous permettent d'apprendre à votre rythme
5. **Validation** : Des checklists vous aident à valider vos acquis avant de passer à la suite

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

## Comment utiliser cette formation

### Pour les débutants

Si vous débutez dans l'IoT et l'AIoT, suivez cette progression :

1. **Commencez par la Room 0** : Elle pose les fondations théoriques et vous familiarise avec l'écosystème IoT/AIoT
2. **Lisez attentivement chaque README** : Ils contiennent toutes les explications nécessaires
3. **Faites les exercices dans l'ordre** : Chaque exercice prépare le suivant
4. **Prenez votre temps** : La compréhension est plus importante que la vitesse
5. **Consultez les ressources** : Des liens vers la documentation officielle sont fournis dans chaque room

### Pour les apprenants expérimentés

Si vous avez déjà de l'expérience :

1. **Consultez les checklists** : Elles vous indiquent rapidement ce que vous devez maîtriser
2. **Allez directement aux labs pratiques** : Les concepts théoriques sont résumés au début de chaque room
3. **Explorez les exercices avancés** : Certains exercices proposent des défis supplémentaires
4. **Adaptez la progression** : Vous pouvez accélérer certaines rooms selon vos besoins

## Structure du dépôt

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

## Démarrage rapide

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.9+** (ou Node.js 18+ selon les rooms)
  - Vérification : `python --version` ou `python3 --version`
  - Téléchargement : https://www.python.org/downloads/
- **Docker** et **Docker Compose** (recommandé pour simplifier l'installation)
  - Vérification : `docker --version` et `docker-compose --version`
  - Téléchargement : https://www.docker.com/get-started
- **Git** (pour cloner le dépôt)
  - Vérification : `git --version`
  - Téléchargement : https://git-scm.com/downloads
- **Terminal** : PowerShell (Windows) ou Terminal (Mac/Linux)

### Pourquoi Docker ?

Docker simplifie grandement l'installation et la configuration :
- **Isolation** : Chaque service fonctionne dans son propre environnement
- **Reproductibilité** : L'environnement est identique pour tous les apprenants
- **Simplicité** : Pas besoin d'installer manuellement chaque service
- **Nettoyage facile** : Vous pouvez supprimer tout l'environnement d'un coup si nécessaire

### Installation avec Docker (Recommandé)

#### Étape 1 : Cloner le dépôt

Cette étape télécharge tous les fichiers de la formation sur votre ordinateur.

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

**Explication** : La commande `git clone` télécharge le dépôt complet. Le dossier `aiot-academy` contiendra tous les fichiers de la formation.

#### Étape 2 : Démarrer les services de base

Cette étape démarre tous les services nécessaires (MQTT broker, base de données, etc.) en arrière-plan.

```powershell
# Windows PowerShell
docker-compose up -d
```

```bash
# Mac/Linux Terminal
docker-compose up -d
```

**Explication** : 
- `docker-compose up` démarre tous les services définis dans le fichier `docker-compose.yml`
- L'option `-d` (detached) permet de lancer les services en arrière-plan, libérant votre terminal
- La première fois, Docker téléchargera les images nécessaires (cela peut prendre quelques minutes)

#### Étape 3 : Vérifier que les services sont actifs

Cette étape vous permet de vérifier que tous les services fonctionnent correctement.

```powershell
# Windows PowerShell
docker-compose ps
```

```bash
# Mac/Linux Terminal
docker-compose ps
```

**Résultat attendu** : Vous devriez voir une liste de services avec le statut "Up" (actif).

**En cas de problème** : Si un service ne démarre pas, consultez la section "Dépannage" ci-dessous ou les logs avec `docker-compose logs <nom-du-service>`.

### Installation sans Docker

Si vous préférez installer les services manuellement (sans Docker), consultez le README de chaque room pour les instructions détaillées. 

**Note** : L'installation sans Docker est plus complexe car vous devrez :
- Installer et configurer chaque service individuellement (Mosquitto, PostgreSQL, etc.)
- Gérer les dépendances et les versions
- Configurer les connexions entre services manuellement

**Recommandation** : Utilisez Docker pour simplifier votre apprentissage, surtout si vous débutez.

## Roadmap de formation

Cette roadmap vous guide à travers les 9 rooms de la formation. Chaque room est conçue pour être complétée indépendamment, mais elles s'appuient les unes sur les autres pour construire progressivement vos compétences.

**Important** : Prenez votre temps pour chaque room. La compréhension est plus importante que la vitesse. Chaque apprenant progresse à son propre rythme.

| Room | Thème | Prérequis | Description |
|------|-------|-----------|-------------|
| [Room 0](room-0-veille-technologique/) | Veille technologique, juridique et réglementaire | Aucun | Fondations théoriques et méthodologiques |
| [Room 1](room-1-foundations/) | Fondations IoT | Room 0 (recommandé) | Bases techniques de l'IoT |
| [Room 2](room-2-iot-protocols-mqtt/) | Protocoles IoT (MQTT) | Room 1 | Communication IoT avec MQTT |
| [Room 3](room-3-data-ingestion-api/) | Ingestion de données (API) | Room 2 | Création d'API REST pour l'IoT |
| [Room 4](room-4-stream-processing-storage/) | Traitement stream et stockage | Room 3 | Traitement de données en temps réel |
| [Room 5](room-5-ml-inference/) | Inférence ML | Room 4 | Intégration de modèles ML |
| [Room 6](room-6-security-aiot/) | Sécurité AIoT | Room 5 | Sécurisation complète des systèmes |
| [Room 7](room-7-observability-mlops-lite/) | Observabilité et MLOps | Room 6 | Monitoring et gestion du cycle de vie ML |
| [Room 8](room-8-capstone-end-to-end/) | Projet final end-to-end | Toutes les rooms | Projet complet intégrant tous les concepts |

## Architecture AIoT de référence

Cette section présente l'architecture globale d'un système AIoT. Vous comprendrez mieux cette architecture au fur et à mesure de votre progression dans les rooms.

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

## Glossaire technique

Ce glossaire définit les termes techniques utilisés dans cette formation. N'hésitez pas à y revenir si vous rencontrez un terme que vous ne comprenez pas.

| Terme | Définition |
|-------|------------|
| **AIoT** | Artificial Intelligence + Internet of Things. Intégration de l'intelligence artificielle dans les systèmes IoT. |
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

## Technologies utilisées

Cette formation utilise des technologies standards de l'industrie pour vous préparer aux environnements professionnels réels.

### Par défaut (si non spécifié dans `/ressource`)

- **MQTT Broker** : Mosquitto (Docker)
- **Simulateurs capteurs** : Python (`paho-mqtt`) ou Node.js (`mqtt`)
- **Backend API** : Node.js (Express) ou Python (FastAPI)
- **Stockage** : SQLite (développement) ou PostgreSQL (production, Docker)
- **ML** : scikit-learn (modèles simples) + endpoint `/predict`
- **Tests** : scripts bash/PowerShell, curl, Postman

## Bonnes pratiques d'apprentissage

Pour tirer le meilleur parti de cette formation, suivez ces bonnes pratiques :

### Organisation de votre apprentissage

1. **Progression séquentielle** : Suivez les rooms dans l'ordre. Chaque room prépare la suivante et construit sur les concepts précédents.

2. **Lecture attentive** : Lisez complètement le README de chaque room avant de commencer les exercices. Les explications théoriques sont essentielles.

3. **Pratique régulière** : Faites tous les exercices et labs. La pratique est la clé de la compréhension.

4. **Validation des acquis** : Utilisez les checklists de validation pour vous assurer que vous maîtrisez les concepts avant de passer à la suite.

5. **Documentation personnelle** : Prenez des notes sur ce que vous apprenez. Cela vous aidera à retenir et à réviser.

### Sécurité et éthique

1. **Environnement local uniquement** : Tout se fait en local avec des données simulées. Aucune clé réelle ou secret de production n'est utilisé.

2. **Conformité** : Respectez les réglementations (RGPD) et les bonnes pratiques de sécurité (OWASP IoT Top 10, NIST).

3. **Éthique** : Les exemples sont purement pédagogiques. Aucune procédure nuisible n'est enseignée.

### Approche pédagogique recommandée

1. **Théorie puis pratique** : Lisez d'abord les concepts théoriques, puis faites les exercices pratiques.

2. **Expérimentation** : N'hésitez pas à modifier le code et à expérimenter. C'est ainsi que vous apprendrez vraiment.

3. **Consultation des solutions** : Essayez d'abord de résoudre les exercices par vous-même avant de consulter les solutions.

4. **Veille continue** : Mettez en place une veille technologique dès la Room 0 et maintenez-la active.

## Sécurité et Éthique

### Environnement pédagogique

Cette formation se déroule entièrement dans un environnement local et sécurisé :

- **Données simulées uniquement** : Toutes les données utilisées sont générées localement pour l'apprentissage
- **Pas de clés réelles** : Aucune clé API, secret ou certificat de production n'est utilisé
- **Pas d'API payantes** : Tous les services sont disponibles localement ou en mode mock
- **Isolation complète** : Rien n'est connecté à Internet ou à des systèmes externes

### Éthique et responsabilité

- **Exemples pédagogiques uniquement** : Tous les exemples sont conçus pour l'apprentissage
- **Aucune procédure nuisible** : Aucune technique d'intrusion, contournement ou sabotage n'est enseignée
- **Respect des réglementations** : La formation respecte les réglementations en vigueur (RGPD, etc.)

### Passage à la production

Lorsque vous passerez à un environnement de production réel, vous devrez :

- Utiliser des certificats émis par une autorité de certification reconnue
- Mettre en place une gestion des secrets professionnelle (AWS Secrets Manager, Azure Key Vault, etc.)
- Implémenter un monitoring de sécurité complet
- Effectuer des audits de sécurité réguliers

## Dépannage

Cette section vous aide à résoudre les problèmes les plus courants. Si vous rencontrez un problème non listé ici, consultez le README de la room concernée ou la section dépannage spécifique.

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

## Contribution

Les contributions sont les bienvenues ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines de contribution.

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

## Remerciements

Ce dépôt pédagogique est inspiré par les meilleures pratiques de l'industrie pour l'AIoT et suit le programme RNCP38920 - Expert des systèmes connectés (IoT).

## Comment soumettre votre travail

### Structure de soumission

Pour chaque room complétée, vous devez créer un dossier avec votre nom dans le format suivant :

```
votre-nom-room-X/
├── README.md              # Votre rapport/notes sur la room
├── code/                  # Votre code source
│   ├── fichiers.py
│   └── ...
├── exercices/             # Vos réponses aux exercices
│   └── exercice-1.md
└── livrables/            # Les livrables demandés (rapports, analyses, etc.)
    └── rapport-veille.md
```

### Étapes pour soumettre votre travail

#### Étape 1 : Préparer votre dossier de travail

1. Créez un dossier avec votre nom et le numéro de la room
   - Exemple : `dupont-room-1/` pour la Room 1
   - Exemple : `martin-room-0/` pour la Room 0

2. Organisez votre travail dans ce dossier :
   - Tous vos fichiers de code
   - Vos réponses aux exercices
   - Les livrables demandés (rapports, analyses, etc.)
   - Un README.md expliquant ce que vous avez fait

#### Étape 2 : Documenter votre travail

Créez un fichier `README.md` dans votre dossier qui explique :

- **Ce que vous avez appris** : Les concepts que vous avez compris
- **Ce que vous avez fait** : Les exercices et labs que vous avez complétés
- **Les difficultés rencontrées** : Les problèmes que vous avez rencontrés et comment vous les avez résolus
- **Les points à améliorer** : Ce que vous aimeriez approfondir

**Exemple de structure de README.md :**

```markdown
# Room X - [Votre nom]

## Ce que j'ai appris

- Concept 1 : [explication]
- Concept 2 : [explication]

## Exercices complétés

- [x] Lab 1 : Simulateur de capteur
- [x] Exercice 1 : Analyse comparative
- [ ] Exercice 2 : [en cours]

## Difficultés rencontrées

- Problème avec... Résolu en...

## Livrables

- [Lien vers vos fichiers]
```

#### Étape 3 : Vérifier avant de soumettre

Avant de soumettre, vérifiez que :

- [ ] Tous vos fichiers sont dans le bon dossier
- [ ] Votre README.md est complet et bien formaté
- [ ] Votre code est commenté et fonctionne
- [ ] Vous avez complété au moins les exercices obligatoires
- [ ] Vous n'avez pas inclus de fichiers sensibles (mots de passe, clés API, etc.)

#### Étape 4 : Soumettre votre travail

**Option 1 : Via Git (recommandé)**

Si vous utilisez Git :

```bash
# Ajouter votre dossier
git add votre-nom-room-X/

# Créer un commit avec un message descriptif
git commit -m "Room X - [Votre nom] - [Description brève]"

# Pousser vers le dépôt
git push origin main
```

**Option 2 : Via fichier compressé**

1. Compressez votre dossier en ZIP
2. Nommez-le : `votre-nom-room-X.zip`
3. Envoyez-le selon les instructions de votre formateur

**Option 3 : Via plateforme d'apprentissage**

Si vous utilisez une plateforme (Moodle, Teams, etc.), suivez les instructions spécifiques de votre formateur.

### Conseils pour une bonne soumission

1. **Soyez organisé** : Une structure claire facilite la correction
2. **Documentez bien** : Expliquez ce que vous avez fait et pourquoi
3. **Testez votre code** : Assurez-vous que tout fonctionne avant de soumettre
4. **Respectez les consignes** : Lisez attentivement ce qui est demandé dans chaque room
5. **Demandez de l'aide si besoin** : N'hésitez pas à poser des questions avant la date limite

### Format des noms de fichiers

Pour faciliter la correction, utilisez des noms de fichiers clairs :

- `temperature_sensor.py` (bon)
- `exercice-1-analyse.md` (bon)
- ❌ `travail.py` (trop vague)
- ❌ `exo1.md` (pas assez descriptif)

### Questions fréquentes

**Q : Dois-je soumettre toutes les rooms en même temps ?**
R : Non, vous pouvez soumettre chaque room au fur et à mesure que vous la complétez.

**Q : Que faire si je n'ai pas terminé tous les exercices ?**
R : Soumettez ce que vous avez fait. Indiquez dans votre README ce qui reste à faire.

**Q : Puis-je travailler en groupe ?**
R : Consultez les instructions de votre formateur. Si le travail de groupe est autorisé, indiquez clairement les membres du groupe dans votre README.

**Q : Que faire si je rencontre un problème technique ?**
R : Documentez le problème dans votre README et essayez de le résoudre. Si vous n'y arrivez pas, demandez de l'aide avant la date limite.

## Support

Pour toute question ou problème :

1. **Consultez les README** : Chaque room contient des explications détaillées et une section dépannage
2. **Vérifiez la section Dépannage** : Les problèmes les plus courants sont documentés ci-dessus
3. **Ouvrez une issue** : Si le dépôt est public, vous pouvez ouvrir une issue pour signaler un problème ou poser une question
4. **Contactez votre formateur** : Pour les questions spécifiques à votre formation

---

**Bon apprentissage !**

