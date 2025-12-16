# Room 6 : Sécurité AIoT

> Sécuriser les systèmes AIoT : identité, secrets, OTA, conformité RGPD

## 📋 Objectifs pédagogiques

À la fin de cette room, vous serez capable de :

- Identifier et analyser les risques de sécurité spécifiques aux systèmes AIoT
- Implémenter l'authentification et l'autorisation pour les devices IoT
- Gérer les secrets de manière sécurisée
- Configurer MQTT avec TLS/SSL
- Mettre en place des mesures de sécurité des données (chiffrement, accès)
- Comprendre et implémenter les mises à jour OTA sécurisées
- Implémenter des ACL (Access Control Lists)
- Intégrer la sécurité dès la conception (Security by Design)
- Analyser les risques et élaborer un plan de gestion des risques
- Assurer la conformité réglementaire (RGPD, sécurité)

## 🎯 Durée estimée

12-16 heures (conforme au programme RNCP38920BC01 - Module 8)

## 📚 Concepts abordés

### Chapitre 1 : Identification des risques de sécurité

- **Risques liés à la sécurité des données**
  - Fuites de données
  - Accès non autorisé
  - Interception des communications
  - Violation de la confidentialité (RGPD)

- **Risques liés à la confidentialité**
  - Exposition de données personnelles
  - Profilage non autorisé
  - Traçabilité excessive

- **Risques liés à la fiabilité des dispositifs**
  - Défaillance des capteurs
  - Manipulation malveillante
  - Déni de service (DoS)

- **Risques liés aux réseaux**
  - Écoute passive (sniffing)
  - Attaques man-in-the-middle
  - Déni de service réseau
  - Vulnérabilités des protocoles

- **Risques liés à la conformité réglementaire**
  - Non-conformité RGPD
  - Sanctions CNIL
  - Atteinte à l'image

### Chapitre 2 : Authentification et Autorisation

- **Certificats X.509 pour devices IoT**
  - Génération de certificats (CA, device certificates)
  - Gestion du cycle de vie des certificats
  - Révocation de certificats (CRL, OCSP)
  - Authentification mutuelle (mTLS)

- **Tokens JWT pour API**
  - Génération et validation de tokens
  - Refresh tokens
  - Scope et permissions
  - Expiration et rotation

- **ACL MQTT**
  - Configuration d'ACL dans Mosquitto
  - Permissions par topic (read, write)
  - Patterns de sécurité des topics

- **Authentification multi-facteurs (MFA)**
  - Pour les interfaces d'administration
  - Pour les accès critiques

### Chapitre 3 : Sécurité des communications

- **TLS/SSL pour MQTT**
  - Configuration TLS dans Mosquitto
  - Certificats serveur et client
  - Versions de TLS (minimum TLS 1.2 recommandé)
  - Cipher suites sécurisés

- **HTTPS pour API**
  - Certificats SSL/TLS
  - HSTS (HTTP Strict Transport Security)
  - Configuration sécurisée des serveurs web

- **Chiffrement des données**
  - Chiffrement symétrique (AES-256)
  - Chiffrement asymétrique (RSA, ECC)
  - Gestion des clés de chiffrement
  - Chiffrement en transit vs au repos

- **VPN et tunnels sécurisés**
  - VPN site-to-site
  - Tunnels IPSec
  - WireGuard pour IoT

### Chapitre 4 : Gestion des secrets

- **Variables d'environnement**
  - Séparation des secrets du code
  - Fichiers .env (jamais committés)
  - Variables d'environnement système

- **Secrets managers (mock/local)**
  - HashiCorp Vault (local)
  - AWS Secrets Manager (mock)
  - Azure Key Vault (mock)
  - Gestion locale avec chiffrement

- **Rotation des clés**
  - Stratégies de rotation
  - Automatisation de la rotation
  - Gestion des versions de clés

- **Stockage sécurisé des secrets**
  - Chiffrement au repos
  - Accès contrôlé
  - Audit des accès

### Chapitre 5 : Sécurité des données et RGPD

- **Chiffrement des données au repos**
  - Chiffrement de base de données
  - Chiffrement au niveau fichier
  - Gestion des clés de chiffrement

- **Anonymisation et pseudonymisation**
  - Techniques d'anonymisation
  - Pseudonymisation réversible
  - Hachage des identifiants

- **Gestion des accès (IAM)**
  - Principe du moindre privilège
  - Contrôle d'accès basé sur les rôles (RBAC)
  - Audit des accès

- **Conformité RGPD**
  - Protection des données personnelles
  - Consentement et bases légales
  - Droits des personnes (accès, rectification, effacement)
  - Privacy by Design et Privacy by Default

### Chapitre 6 : Mises à jour OTA sécurisées

- **Stratégies de déploiement**
  - Rollout progressif (canary, blue-green)
  - Groupes de déploiement
  - Vérification préalable

- **Vérification d'intégrité**
  - Signature des firmware (cryptographique)
  - Vérification de hash (SHA-256)
  - Certificats de signature

- **Rollback**
  - Stratégies de rollback
  - Conservation des versions précédentes
  - Tests de rollback

- **Communication sécurisée**
  - TLS pour les mises à jour
  - Authentification du serveur de mise à jour
  - Protection contre les attaques

### Chapitre 7 : Security by Design

- **Intégration de la sécurité dès la conception**
  - Threat modeling
  - Security requirements
  - Architecture sécurisée

- **Hardening des systèmes**
  - Configuration sécurisée par défaut
  - Désactivation des services inutiles
  - Mise à jour régulière des composants

- **Tests de sécurité**
  - Tests de pénétration
  - Tests de vulnérabilités
  - Code review sécurité
  - Analyse statique de code (SAST)

### Chapitre 8 : Gestion des incidents et conformité

- **Détection et réponse aux incidents**
  - Monitoring de sécurité
  - Détection d'anomalies
  - Réponse aux incidents
  - Plan de continuité

- **Conformité réglementaire**
  - ISO/IEC 27001 (sécurité de l'information)
  - IEC 62443 (sécurité industrielle)
  - RGPD
  - Bonnes pratiques (NIST Cybersecurity Framework)

- **Audit et reporting**
  - Audit de sécurité régulier
  - Reporting de conformité
  - Traçabilité des actions

## 🏃 Labs pratiques

### Lab 1 : Configuration MQTT avec TLS

**Objectif** : Sécuriser les communications MQTT avec TLS

**Étapes** :
1. Générer un certificat CA (Certificate Authority)
2. Générer un certificat serveur pour Mosquitto
3. Générer des certificats clients pour les devices
4. Configurer Mosquitto pour utiliser TLS
5. Tester la connexion sécurisée

**Livrables** :
- Configuration Mosquitto avec TLS
- Scripts de génération de certificats
- Documentation de configuration

### Lab 2 : Authentification avec certificats X.509

**Objectif** : Implémenter l'authentification mutuelle (mTLS)

**Étapes** :
1. Configurer Mosquitto pour authentification par certificat
2. Créer un client MQTT avec certificat client
3. Tester l'authentification
4. Implémenter la révocation de certificat (CRL)

**Livrables** :
- Client MQTT avec authentification par certificat
- Configuration CRL
- Tests de validation

### Lab 3 : Gestion des secrets avec Vault (local)

**Objectif** : Mettre en place un gestionnaire de secrets local

**Étapes** :
1. Installer HashiCorp Vault (mode dev)
2. Stocker des secrets (clés API, mots de passe)
3. Récupérer des secrets depuis l'application
4. Implémenter la rotation des secrets

**Livrables** :
- Configuration Vault
- Scripts d'intégration
- Documentation d'utilisation

### Lab 4 : Chiffrement des données

**Objectif** : Chiffrer les données en transit et au repos

**Étapes** :
1. Chiffrer les données en transit (TLS)
2. Chiffrer les données au repos dans la base de données
3. Implémenter la gestion des clés de chiffrement
4. Tester le chiffrement/déchiffrement

**Livrables** :
- Scripts de chiffrement
- Configuration de chiffrement DB
- Tests de validation

### Lab 5 : Analyse de risques et plan de sécurité

**Objectif** : Réaliser une analyse de risques pour une solution IoT

**Étapes** :
1. Identifier les actifs (devices, données, systèmes)
2. Identifier les menaces
3. Évaluer les vulnérabilités
4. Calculer les risques
5. Proposer des mesures de mitigation

**Livrables** :
- Analyse de risques (document)
- Cartographie des risques
- Plan de mitigation

## 📖 Exercices

### Exercice 1 : Identification des risques

**Objectif** : Identifier les risques pour un système IoT de monitoring environnemental

**Consigne** :
Analyser un système IoT fictif et identifier :
- 5 risques liés à la sécurité des données
- 3 risques liés aux réseaux
- 2 risques liés à la conformité réglementaire

**Livrable** : Document d'analyse des risques (3-5 pages)

### Exercice 2 : Plan de gestion des risques

**Objectif** : Élaborer un plan de gestion des risques

**Consigne** :
Pour les risques identifiés dans l'exercice 1 :
- Définir des mesures préventives
- Définir des mesures correctives
- Identifier les responsables
- Définir des indicateurs de suivi

**Livrable** : Plan de gestion des risques (5-7 pages)

### Exercice 3 : Politique de sécurité

**Objectif** : Rédiger une politique de sécurité pour une solution AIoT

**Consigne** :
Rédiger une politique de sécurité incluant :
- Objectifs de sécurité
- Rôles et responsabilités
- Mesures techniques et organisationnelles
- Gestion des incidents
- Formation et sensibilisation

**Livrable** : Politique de sécurité (8-10 pages)

## ⚠️ Important

**Environnement pédagogique uniquement** :
- Tout se fait en environnement local avec données simulées
- Aucune clé réelle de production n'est utilisée
- Les certificats sont auto-signés (pour l'apprentissage)
- Les secrets sont stockés localement (jamais en production)

**Bonnes pratiques en production** :
- Utiliser des certificats émis par une CA reconnue
- Utiliser un gestionnaire de secrets en production (AWS Secrets Manager, Azure Key Vault)
- Mettre en place un monitoring de sécurité
- Effectuer des audits de sécurité réguliers

## 📚 Ressources

### Documentation
- **OWASP IoT Top 10** : https://owasp.org/www-project-internet-of-things/
- **NIST Cybersecurity Framework** : https://www.nist.gov/cyberframework
- **IEC 62443** : Sécurité des systèmes industriels
- **CNIL - Sécurité des données** : https://www.cnil.fr/fr/securite-des-donnees

### Outils
- **Mosquitto** : Broker MQTT avec support TLS
- **HashiCorp Vault** : Gestionnaire de secrets
- **OpenSSL** : Génération de certificats
- **OWASP ZAP** : Tests de sécurité

## ✅ Checklist de validation

Avant de passer à la Room 7, assurez-vous d'avoir :

- [ ] Compris les principaux risques de sécurité IoT/AIoT
- [ ] Configuré MQTT avec TLS
- [ ] Implémenté l'authentification par certificat
- [ ] Mis en place une gestion des secrets
- [ ] Réalisé une analyse de risques
- [ ] Élaboré un plan de gestion des risques
- [ ] Compris les aspects de conformité RGPD liés à la sécurité

## ➡️ Suite

Une fois cette room terminée, passez à [Room 7 : Observabilité et MLOps](../room-7-observability-mlops-lite/).

