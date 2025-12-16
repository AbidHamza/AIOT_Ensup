# Dépannage - Room 1 : Fondations IoT

## Erreurs fréquentes et solutions

### Python non trouvé

**Erreur :** `'python' n'est pas reconnu comme commande`

**Solution Windows PowerShell :**
```powershell
# Vérifier l'installation
python --version
# Si non installé, utiliser python3
python3 --version
```

**Solution Mac/Linux Terminal :**
```bash
# Utiliser python3 explicitement
python3 temperature_sensor.py
```

### Module non trouvé

**Erreur :** `ModuleNotFoundError: No module named 'numpy'`

**Solution :**
```powershell
# Windows PowerShell
pip install -r requirements.txt
# Ou avec python3
python3 -m pip install -r requirements.txt
```

```bash
# Mac/Linux Terminal
pip3 install -r requirements.txt
```

### Environnement virtuel non activé

**Erreur :** Packages installés mais toujours des erreurs d'import

**Solution :**
```powershell
# Windows PowerShell
cd room-1-foundations/src
.\venv\Scripts\Activate.ps1
```

```bash
# Mac/Linux Terminal
cd room-1-foundations/src
source venv/bin/activate
```

### Problème de permissions (Mac/Linux)

**Erreur :** `Permission denied` lors de l'installation

**Solution :**
```bash
# Utiliser --user
pip3 install --user -r requirements.txt
```

---

Pour d'autres problèmes, consultez le README principal ou ouvrez une issue.

