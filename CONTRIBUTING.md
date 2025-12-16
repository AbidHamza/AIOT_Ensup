# Guide de contribution

Merci de votre intérêt pour contribuer à AIoT Academy ! Ce document décrit les guidelines pour contribuer au projet.

## 🎯 Objectifs de contribution

- Améliorer la clarté pédagogique
- Corriger des erreurs ou bugs
- Ajouter des exercices ou labs
- Améliorer la documentation
- Traduire du contenu (si applicable)

## 📝 Format de contribution

### Structure des rooms

Chaque room doit contenir :

```
room-X-name/
├── README.md           # Documentation principale (objectifs, concepts, instructions)
├── scenarios/          # Scénarios pédagogiques
├── exercises/          # Exercices guidés
├── checklists/         # Checklists de validation
├── src/                # Code source des labs
├── tests/              # Scripts de test
└── troubleshooting.md  # Erreurs fréquentes et solutions
```

### Standards de code

- **Python** : PEP 8, type hints quand possible
- **JavaScript/Node.js** : ESLint, JSDoc pour les fonctions
- **Commentaires** : En français pour la pédagogie
- **Nommage** : Variables/fonctions en anglais, commentaires/doc en français

### Documentation

- **README.md** : Toujours très guidé, avec exemples Windows PowerShell + Mac/Linux Terminal
- **Code comments** : Explications pédagogiques en français
- **Markdown** : Format standard, avec table des matières

## 🔄 Processus de contribution

1. **Fork** le dépôt (si applicable)
2. **Créer une branche** pour votre modification (`git checkout -b feature/ma-contribution`)
3. **Faire vos modifications** en suivant les standards
4. **Tester** vos modifications (labs exécutables)
5. **Commit** avec un message clair (`git commit -m "Ajout: description"`)
6. **Push** vers votre branche (`git push origin feature/ma-contribution`)
7. **Ouvrir une Pull Request** avec description détaillée

### Messages de commit

Format recommandé :
```
Type: Description courte (50 caractères max)

Description détaillée (optionnelle, 72 caractères par ligne)

Types possibles:
- Ajout: Nouvelle fonctionnalité
- Fix: Correction de bug
- Doc: Modification documentation
- Refactor: Refactorisation code
- Test: Ajout/modification tests
```

## ✅ Checklist avant contribution

- [ ] Code testé localement (Docker et sans Docker)
- [ ] Documentation mise à jour (README.md)
- [ ] Pas de secrets/clés en dur
- [ ] Code conforme aux standards (lint)
- [ ] Commentaires pédagogiques en français
- [ ] Instructions Windows PowerShell + Mac/Linux Terminal

## 🚫 À éviter

- ❌ Secrets ou clés API réelles
- ❌ Procédures nuisibles (intrusion, contournement)
- ❌ Contenu non pédagogique
- ❌ Code non commenté ou non testé
- ❌ Documentation uniquement pour un OS

## 📚 Ressources

- Consulter `/ressource` pour les guidelines pédagogiques détaillées
- Vérifier la structure existante des rooms avant de créer une nouvelle
- Suivre le format JSON/MQTT défini dans l'architecture de référence

## 🤝 Code de conduite

- Respecter les autres contributeurs
- Être constructif dans les critiques
- Focus sur la pédagogie et la clarté
- Maintenir un environnement d'apprentissage positif

---

Merci de contribuer à AIoT Academy ! 🎓

