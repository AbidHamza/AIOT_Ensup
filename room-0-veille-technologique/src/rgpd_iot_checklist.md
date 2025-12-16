# Checklist RGPD pour solutions IoT/AIoT

## 📋 Conformité RGPD - Points essentiels

Cette checklist vous aide à vérifier la conformité RGPD de votre solution IoT.

### 1. Identification des données personnelles

- [ ] **Cartographie des données collectées**
  - [ ] Quelles données sont collectées ? (température, localisation, comportement, etc.)
  - [ ] Ces données permettent-elles d'identifier directement une personne ? (nom, email, etc.)
  - [ ] Ces données permettent-elles d'identifier indirectement une personne ? (adresse IP, identifiant unique device, etc.)

- [ ] **Classification des données**
  - [ ] Données directement identifiantes (nom, prénom, email)
  - [ ] Données indirectement identifiantes (ID device, adresse MAC, IP)
  - [ ] Données sensibles (santé, géolocalisation précise)
  - [ ] Données pseudonymisées

### 2. Bases légales du traitement

- [ ] **Consentement**
  - [ ] Le consentement est-il libre, spécifique, éclairé et univoque ?
  - [ ] Le consentement peut-il être retiré facilement ?
  - [ ] Le consentement est-il documenté ?

- [ ] **Autres bases légales possibles**
  - [ ] Exécution d'un contrat
  - [ ] Obligation légale
  - [ ] Intérêt légitime (avec analyse d'impact)
  - [ ] Protection des intérêts vitaux
  - [ ] Mission d'intérêt public

### 3. Principes fondamentaux

- [ ] **Licéité, loyauté, transparence**
  - [ ] Le traitement est-il licite ?
  - [ ] Les personnes sont-elles informées ?
  - [ ] Les informations sont-elles claires et compréhensibles ?

- [ ] **Finalité**
  - [ ] La finalité est-elle déterminée, explicite et légitime ?
  - [ ] Le traitement respecte-t-il la finalité initiale ?
  - [ ] En cas d'évolution, la nouvelle finalité est-elle compatible ?

- [ ] **Minimisation**
  - [ ] Seules les données nécessaires sont-elles collectées ?
  - [ ] La durée de conservation est-elle limitée ?
  - [ ] Les données sont-elles supprimées quand elles ne sont plus nécessaires ?

- [ ] **Exactitude**
  - [ ] Des mécanismes de correction sont-ils en place ?
  - [ ] Les données sont-elles mises à jour si nécessaire ?

- [ ] **Limitation de la conservation**
  - [ ] Durée de conservation définie ?
  - [ ] Critères objectifs de suppression ?
  - [ ] Archivage conforme si nécessaire ?

- [ ] **Intégrité et confidentialité**
  - [ ] Chiffrement des données en transit ?
  - [ ] Chiffrement des données au repos ?
  - [ ] Contrôle d'accès ?
  - [ ] Audit de sécurité régulier ?

### 4. Droits des personnes

- [ ] **Droit d'information**
  - [ ] Information préalable fournie ?
  - [ ] Mentions RGPD présentes (qui, pourquoi, combien de temps, etc.) ?
  - [ ] Information accessible et compréhensible ?

- [ ] **Droit d'accès**
  - [ ] Mécanisme pour demander les données ?
  - [ ] Délai de réponse (1 mois) respecté ?
  - [ ] Format lisible fourni ?

- [ ] **Droit de rectification**
  - [ ] Possibilité de corriger les données ?
  - [ ] Délai de réponse respecté ?

- [ ] **Droit à l'effacement ("droit à l'oubli")**
  - [ ] Mécanisme de suppression des données ?
  - [ ] Cas d'exception identifiés et documentés ?
  - [ ] Information aux sous-traitants pour suppression ?

- [ ] **Droit à la limitation du traitement**
  - [ ] Possibilité de limiter le traitement ?
  - [ ] Processus de limitation opérationnel ?

- [ ] **Droit à la portabilité**
  - [ ] Export des données dans un format structuré ?
  - [ ] Export automatisé si possible ?

- [ ] **Droit d'opposition**
  - [ ] Possibilité de s'opposer au traitement ?
  - [ ] Cas d'exception identifiés ?

- [ ] **Droit de ne pas faire l'objet d'une décision automatisée**
  - [ ] Profilage identifié ?
  - [ ] Décisions automatisées identifiées ?
  - [ ] Droit de contestation prévu ?

### 5. Responsabilités et rôles

- [ ] **Responsable de traitement**
  - [ ] Rôle identifié et documenté ?
  - [ ] Registre des activités de traitement tenu ?

- [ ] **Sous-traitants**
  - [ ] Tous les sous-traitants identifiés ?
  - [ ] Contrats avec clauses RGPD ?
  - [ ] Vérification de conformité des sous-traitants ?

- [ ] **Co-responsables de traitement**
  - [ ] Accords de co-responsabilité documentés ?
  - [ ] Répartition des responsabilités claire ?

### 6. Sécurité des données

- [ ] **Mesures techniques**
  - [ ] Chiffrement des données en transit (TLS, VPN)
  - [ ] Chiffrement des données au repos
  - [ ] Authentification forte
  - [ ] Contrôle d'accès (IAM, ACL)
  - [ ] Journalisation des accès
  - [ ] Sauvegardes sécurisées

- [ ] **Mesures organisationnelles**
  - [ ] Politique de sécurité documentée
  - [ ] Formation du personnel
  - [ ] Gestion des accès (principe du moindre privilège)
  - [ ] Procédures d'incident
  - [ ] Tests de sécurité réguliers

- [ ] **Privacy by Design**
  - [ ] Intégration de la protection des données dès la conception ?
  - [ ] Minimisation des données par défaut ?
  - [ ] Transparence et contrôle utilisateur ?

- [ ] **Privacy by Default**
  - [ ] Paramètres les plus protecteurs par défaut ?
  - [ ] Pas de traitement au-delà du nécessaire ?

### 7. Notification des violations

- [ ] **Procédure de notification**
  - [ ] Procédure documentée ?
  - [ ] Délai de 72h connu et applicable ?
  - [ ] Personne responsable identifiée ?

- [ ] **Communication aux personnes**
  - [ ] Communication si risque élevé ?
  - [ ] Template de communication préparé ?

### 8. Analyse d'impact (DPIA - Data Protection Impact Assessment)

- [ ] **DPIA réalisé si nécessaire**
  - [ ] Évaluation systématique ?
  - [ ] Profilage à grande échelle ?
  - [ ] Surveillance systématique ?
  - [ ] Données sensibles à grande échelle ?

- [ ] **Contenu du DPIA**
  - [ ] Description du traitement
  - [ ] Évaluation de la nécessité et proportionnalité
  - [ ] Évaluation des risques
  - [ ] Mesures de mitigation
  - [ ] Consultation DPO si applicable

### 9. DPO (Data Protection Officer)

- [ ] **DPO désigné si nécessaire**
  - [ ] Traitement à grande échelle de données sensibles ?
  - [ ] Surveillance systématique à grande échelle ?
  - [ ] Autorité publique ?

- [ ] **Rôle du DPO**
  - [ ] Information et conseil
  - [ ] Contrôle de conformité
  - [ ] Point de contact avec l'autorité

### 10. Transferts internationaux

- [ ] **Transferts hors UE identifiés**
  - [ ] Où sont stockées/traitées les données ?
  - [ ] Pays tiers concernés ?

- [ ] **Garanties appropriées**
  - [ ] Décision d'adéquation de la Commission ?
  - [ ] Clauses contractuelles types (SCC) ?
  - [ ] Binding Corporate Rules (BCR) ?
  - [ ] Autres garanties (certifications, codes de conduite) ?

### 11. Documentation

- [ ] **Registre des activités de traitement**
  - [ ] Tenu à jour ?
  - [ ] Accessible à la CNIL sur demande ?
  - [ ] Contenu complet (finalités, catégories de personnes, etc.) ?

- [ ] **Documentation des mesures**
  - [ ] Mesures techniques documentées
  - [ ] Mesures organisationnelles documentées
  - [ ] Procédures documentées

### 12. Audit et amélioration continue

- [ ] **Audit de conformité**
  - [ ] Audit interne régulier ?
  - [ ] Audit externe si nécessaire ?
  - [ ] Actions correctives planifiées ?

- [ ] **Veille réglementaire**
  - [ ] Veille sur évolutions RGPD
  - [ ] Adaptation des pratiques

## 📝 Ressources complémentaires

- **CNIL - Guide RGPD** : https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on
- **CNIL - IoT et données personnelles** : https://www.cnil.fr/fr/objets-connectes-et-donnees-personnelles
- **EDPB Guidelines** : https://edpb.europa.eu/our-work-tools/general-guidance/gdpr-guidelines-recommendations-best-practices_fr

## ⚠️ Points d'attention spécifiques IoT

1. **Capteurs et données indirectes** : Un capteur de température dans un logement peut révéler des données personnelles (présence, habitudes)

2. **Géolocalisation** : Données très sensibles, nécessite consentement explicite

3. **Données de santé** : Catégorie particulière de données sensibles, réglementation renforcée

4. **Profilage** : Analyse comportementale automatisée, droits spécifiques

5. **Edge computing** : Données traitées localement, mais toujours soumises au RGPD si données personnelles

6. **Consentement device** : Comment obtenir un consentement valide sur un objet connecté avec interface limitée ?

