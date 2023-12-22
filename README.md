# sae3.02_monitoring
SAE 3.02, création d'une application graphique de monitoring d'ordinateurs.

## 1. Installation

### 1.1 Création du site HTML statique

Il faut d'abord commencer par générer la documentation Sphinx, qui nous sera utile par la suite.

1. Se placer dans le répertoire principal `sae3.02_monitoring`
2. Ouvrir un terminal dans ce répertoire
3. Changez les droits d'exécution du programme bash : `chmod +x sphinx-build.sh`
4. Lancez le programme bash : `./sphinx-build.sh`

### 1.2 Installation des modules requis

- Méthode 1 : Rendez-vous sur la page `Configuration` > `Preinstallation` du site Web généré par Sphinx et installez tous les modules cités
- Méthode 2 :
    - Se placer dans le répertoire principal `sae3.02_monitoring`
    - Ouvrir un terminal dans ce répertoire
    - Changez les droits d'exécution du programme bash : `chmod +x installation-modules.sh`
    - Lancez le programme bash : `./installation-modules.sh` 

### 1.3 Installation de la base de données

Rendez-vous sur la page `Documentation` > `PostgreSQL` du site Web généré par Sphinx et installez la base de données PostgreSQL en suivant les indications

### 1.4 Installation de l'application cliente

1. Sélectionnez les fichiers `client.py` et `recuperation.py` (situés dans `sae3.02_monitoring`) et positionnez les sur la machine cliente (dans le même répertoire)
2. Dans `client.py` ligne 12, remplacez `localhost` de `'host': 'localhost',` par l'adresse IP de la machine contenant la base de données PostgreSQL
3. Lancez le programme `client.py`

### 1.5 Installation du panel administrateur

1. Sélectionnez les fichiers `dashboard.py` et `graph.py` (situés dans `sae3.02_monitoring`) et positionnez les sur la machine cliente (dans le même répertoire)
2. Dans `dashboard.py` ligne 12, remplacez `localhost` de `host="localhost",` par l'adresse IP de la machine contenant la base de données PostgreSQL
3. Lancez le programme `dashboard.py`