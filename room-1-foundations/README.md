# Room 1 : Fondations IoT

> Bases de l'IoT : capteurs, simulateurs, concepts fondamentaux

## Objectifs pédagogiques

À la fin de cette room, vous serez capable de :

- Comprendre les concepts fondamentaux de l'IoT et leur application pratique
- Simuler des capteurs IoT (température, humidité, pression, etc.) avec Python
- Générer des données de capteurs réalistes qui imitent le comportement de vrais capteurs
- Visualiser les données capteurs en temps réel pour comprendre leur évolution
- Comprendre l'architecture d'un système IoT simple et ses composants

## À propos de cette room

Cette room est conçue pour être complétée à votre propre rythme. Prenez le temps nécessaire pour bien comprendre chaque concept avant de passer au suivant. Il n'y a pas de limite de temps - l'important est la compréhension.

## Pourquoi cette room est importante

Cette room pose les fondations essentielles pour comprendre l'IoT. Avant de travailler avec des protocoles complexes ou des architectures avancées, il est crucial de comprendre :

- **Comment fonctionnent les capteurs** : Les capteurs sont les yeux et les oreilles d'un système IoT
- **Comment générer des données réalistes** : Pour développer et tester sans matériel physique coûteux
- **Comment structurer les données** : Une bonne structure de données facilite tout le reste du pipeline

**Sans ces bases**, vous aurez du mal à comprendre les rooms suivantes qui construisent sur ces concepts.

## Concepts abordés

### 1. Introduction à l'IoT

**Qu'est-ce que l'IoT ?**

L'Internet des Objets (IoT) désigne l'interconnexion d'objets physiques avec Internet. Ces objets peuvent collecter, transmettre et recevoir des données, permettant ainsi leur contrôle et leur surveillance à distance.

**Composants d'un système IoT**

Un système IoT complet comprend généralement :

- **Capteurs** : Collectent des données de l'environnement (température, humidité, mouvement, etc.)
- **Actionneurs** : Exécutent des actions physiques (allumer une lumière, ouvrir une vanne, etc.)
- **Gateway** : Point d'entrée qui connecte les devices locaux au cloud
- **Cloud/Backend** : Traite, stocke et analyse les données collectées
- **Interface utilisateur** : Permet aux utilisateurs de visualiser et contrôler le système

**Cas d'usage IoT**

- Domotique : Maison intelligente avec contrôle de l'éclairage, du chauffage, etc.
- Industrie : Monitoring de machines, maintenance prédictive
- Agriculture : Irrigation intelligente, monitoring des cultures
- Santé : Monitoring de patients à domicile
- Transport : Gestion de flotte, véhicules connectés

### 2. Capteurs IoT

**Types de capteurs courants**

- **Température** : Mesure la température ambiante (ex: DHT22, DS18B20)
- **Humidité** : Mesure l'humidité relative de l'air
- **Pression** : Mesure la pression atmosphérique (ex: BMP280)
- **Accéléromètre** : Détecte les mouvements et vibrations
- **GPS** : Détermine la position géographique
- **Caméra** : Capture des images ou vidéos

**Caractéristiques importantes des capteurs**

- **Résolution** : La plus petite variation que le capteur peut détecter
- **Précision** : L'écart entre la valeur mesurée et la valeur réelle
- **Plage de mesure** : Les valeurs min et max que le capteur peut mesurer
- **Temps de réponse** : Le temps nécessaire pour que le capteur réagisse à un changement
- **Fréquence d'échantillonnage** : Le nombre de mesures par seconde

**Format de données capteurs**

Les données de capteurs sont généralement structurées en JSON pour faciliter leur traitement :

```json
{
  "sensor_id": "TEMP-001",
  "sensor_type": "temperature",
  "value": 22.3,
  "unit": "celsius",
  "timestamp": "2025-01-15T10:30:45Z",
  "location": "room-101"
}
```

### 3. Simulation de capteurs

**Pourquoi simuler des capteurs ?**

La simulation est essentielle pour le développement et les tests :

- **Coût** : Évite d'acheter du matériel coûteux pour chaque test
- **Rapidité** : Permet de développer et tester rapidement sans attendre le matériel
- **Reproductibilité** : Les données simulées sont reproductibles, facilitant les tests
- **Contrôle** : Vous pouvez générer des scénarios spécifiques (valeurs extrêmes, pannes, etc.)
- **Scalabilité** : Facile de simuler des centaines de capteurs simultanément

**Modèles de données réalistes**

Pour simuler des capteurs de manière réaliste, il faut :

- **Variation naturelle** : Ajouter du bruit aléatoire pour imiter les variations naturelles
- **Tendances** : Simuler des tendances (température qui augmente le jour, diminue la nuit)
- **Plages réalistes** : Respecter les plages de valeurs réalistes (température entre -10°C et 40°C pour l'intérieur)
- **Timestamps cohérents** : Utiliser des timestamps réels et cohérents

**Génération de séries temporelles**

Une série temporelle est une séquence de données mesurées à intervalles réguliers. Pour la générer :

1. Définir une valeur de base (ex: température moyenne de 20°C)
2. Ajouter une tendance (ex: variation quotidienne)
3. Ajouter du bruit aléatoire pour réalisme
4. Respecter les contraintes physiques (ex: température ne peut pas changer instantanément de 10°C)

## Prérequis

Avant de commencer cette room, assurez-vous d'avoir :

- **Python 3.9+ installé**
  - Vérification : `python --version` ou `python3 --version`
  - Si non installé : https://www.python.org/downloads/
- **pip installé** (généralement inclus avec Python)
  - Vérification : `pip --version` ou `pip3 --version`
- **(Optionnel) Docker et Docker Compose** : Utile si vous voulez utiliser les services Docker, mais pas obligatoire pour cette room

**Note** : Si vous avez terminé la Room 0, vous devriez déjà avoir ces outils installés.

## Installation

### Étape 1 : Naviguer vers le dossier de la room

```powershell
# Windows PowerShell
cd room-1-foundations/src
```

```bash
# Mac/Linux Terminal
cd room-1-foundations/src
```

**Explication** : Le dossier `src` contient tous les fichiers de code source pour cette room.

### Étape 2 : Créer un environnement virtuel Python

Un environnement virtuel isole les dépendances de ce projet des autres projets Python sur votre machine.

```powershell
# Windows PowerShell
python -m venv venv
```

```bash
# Mac/Linux Terminal
python3 -m venv venv
```

**Explication** : Cette commande crée un dossier `venv` contenant un environnement Python isolé.

### Étape 3 : Activer l'environnement virtuel

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bash
# Mac/Linux Terminal
source venv/bin/activate
```

**Résultat attendu** : Votre invite de commande devrait maintenant afficher `(venv)` au début, indiquant que l'environnement virtuel est actif.

**Note** : Si vous obtenez une erreur sur PowerShell concernant l'exécution de scripts, exécutez d'abord :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Étape 4 : Installer les dépendances

```powershell
# Windows PowerShell (avec venv activé)
pip install -r requirements.txt
```

```bash
# Mac/Linux Terminal (avec venv activé)
pip install -r requirements.txt
```

**Explication** : Cette commande installe toutes les bibliothèques Python nécessaires listées dans le fichier `requirements.txt`.

**Résultat attendu** : Vous devriez voir les packages s'installer un par un. L'installation peut prendre quelques minutes la première fois.

## Navigation dans cette room

Cette room est organisée de manière à faciliter votre apprentissage :

1. **Commencez par lire cette section** : Comprendre les concepts théoriques
2. **Passez à l'installation** : Configurez votre environnement de travail
3. **Faites les labs dans l'ordre** : Chaque lab construit sur le précédent
4. **Validez vos acquis** : Utilisez la checklist avant de passer à la suite

## Structure de la room

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

## Lab 1 : Simulateur de capteur de température

### Objectif

Créer un simulateur simple qui génère des données de température réalistes. Ce lab vous apprend à :
- Générer des données de capteur avec Python
- Structurer les données de manière cohérente
- Ajouter des timestamps aux données

### Comprendre le code

Avant d'exécuter le code, examinons ce qu'il fait :

1. **Importation des bibliothèques** : Le code utilise `random` pour générer des valeurs aléatoires et `datetime` pour les timestamps
2. **Génération de données** : Une fonction génère une température réaliste (entre 18°C et 25°C pour l'intérieur)
3. **Formatage** : Les données sont formatées de manière lisible pour l'affichage

### Exécution

Assurez-vous d'être dans le dossier `src` avec l'environnement virtuel activé :

```powershell
# Windows PowerShell
python temperature_sensor.py
```

```bash
# Mac/Linux Terminal
python3 temperature_sensor.py
```

### Résultat attendu

Vous devriez voir s'afficher des données de température toutes les secondes :

```
Sensor ID: TEMP-001
Temperature: 22.3°C
Timestamp: 2025-01-15 10:30:45
---
Sensor ID: TEMP-001
Temperature: 22.5°C
Timestamp: 2025-01-15 10:30:46
---
```

**Pour arrêter** : Appuyez sur `Ctrl+C` dans le terminal.

### Analyse du résultat

- **Sensor ID** : Identifiant unique du capteur (utile quand vous avez plusieurs capteurs)
- **Temperature** : Valeur générée de manière réaliste (varie légèrement entre les mesures)
- **Timestamp** : Date et heure précises de la mesure (essentiel pour l'analyse temporelle)

### Exercice pratique

Modifiez le code pour :
1. Changer la plage de température (ex: entre 15°C et 30°C)
2. Ajouter un capteur d'humidité qui génère des valeurs entre 40% et 60%
3. Modifier la fréquence d'échantillonnage (ex: toutes les 5 secondes au lieu de 1 seconde)

## Lab 2 : Visualisation en temps réel

### Objectif

Visualiser les données de plusieurs capteurs en temps réel avec matplotlib. Ce lab vous apprend à :
- Créer des graphiques en temps réel
- Visualiser plusieurs séries de données simultanément
- Comprendre l'évolution des données dans le temps

### Pourquoi visualiser les données ?

La visualisation est essentielle pour :
- **Comprendre les tendances** : Voir comment les données évoluent dans le temps
- **Détecter les anomalies** : Identifier rapidement des valeurs anormales
- **Valider la simulation** : Vérifier que les données générées sont réalistes
- **Présenter les résultats** : Communiquer efficacement les données à d'autres personnes

### Exécution

Assurez-vous d'avoir installé matplotlib (il devrait être dans requirements.txt) :

```powershell
# Windows PowerShell
python visualizer.py
```

```bash
# Mac/Linux Terminal
python3 visualizer.py
```

### Résultat attendu

Une fenêtre graphique devrait s'ouvrir affichant :
- Un graphique en temps réel avec les valeurs de température
- L'axe X représentant le temps
- L'axe Y représentant la température en degrés Celsius
- La courbe se mettant à jour automatiquement

**Note** : Si le fichier `visualizer.py` n'existe pas encore, vous pouvez le créer comme exercice en utilisant matplotlib.

## Checklist de validation

Avant de passer à la Room 2, assurez-vous d'avoir complété :

- [ ] J'ai compris les concepts fondamentaux de l'IoT
- [ ] Je peux simuler un capteur de température
- [ ] Je peux générer des données réalistes pour plusieurs capteurs
- [ ] Je peux visualiser les données en temps réel
- [ ] J'ai complété tous les exercices pratiques
- [ ] J'ai documenté mon travail dans un README.md

**Note** : Si vous n'avez pas complété tous les éléments, ce n'est pas grave. Vous pouvez toujours passer à la suite et revenir plus tard si nécessaire.

## Dépannage

Si vous rencontrez des problèmes :

1. **Consultez le fichier troubleshooting.md** : Il contient les solutions aux problèmes les plus courants
2. **Vérifiez votre installation** : Assurez-vous que Python et les dépendances sont correctement installés
3. **Vérifiez les logs d'erreur** : Les messages d'erreur Python sont généralement très explicites

## Ressources supplémentaires

Pour approfondir vos connaissances :

- [IoT Fundamentals](https://www.iotforall.com/what-is-iot) : Introduction complète à l'IoT
- [Sensor Types](https://www.electronicsforu.com/technology-trends/iot-sensors-types) : Types de capteurs IoT

## Comment soumettre votre travail

Voir la section "Comment soumettre votre travail" dans le [README principal](../../README.md#comment-soumettre-votre-travail) pour les instructions détaillées.

**Rappel** : Créez un dossier `votre-nom-room-1/` avec votre code, vos exercices et un README.md expliquant ce que vous avez fait.

## Suite

Une fois cette room terminée et validée, vous pouvez passer à :

- **[Room 2 : Protocoles IoT (MQTT)](../room-2-iot-protocols-mqtt/)** : Apprendre à communiquer avec MQTT

**Conseil** : Ne passez à la Room 2 que lorsque vous êtes à l'aise avec les concepts de la Room 1.

