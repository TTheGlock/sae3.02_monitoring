=============================================
Organisation des fichiers
=============================================

Dans cette documentation, vous allez retrouver des explications sur les fichiers présents dans ce projet.

--------------------------------------------
Organisation des fichiers du dossier principal ``sae3.02_monitoring``
--------------------------------------------

.. code-block:: bash

    └── sae3.02_monitoring
        ├── client.py
        ├── dashboard.py
        ├── graph.py
        └── recuperation.py

* ``client.py`` = programme python utilisé pour ouvrir une connexion avec une base de données PostgreSQL et y insérer des données récupérées via le module ``recuperation_data`` du fichier ``recuperation.py``

* ``dashboard.py`` = programme python utilisé pour ouvrir une connexion avec une base de données PostgreSQL, y récupérer des données, et les afficher graphiquement notamment par des graphiques via le module ``graph_1`` du fichier ``graph.py``

* ``graph.py`` = programme python de création de graphique(s) | utilisé par le programme ``dashboard.py``

* ``recuperation.py`` = programme python de récupération de caractéristiques de composants informatiques  | utilisé par le programme ``client.py``

--------------------------------------------
Organisation des fichiers du dossier ``docs``
--------------------------------------------

.. code-block:: bash

    └── docs
        ├── build
        │   └── not_empty.txt
        ├── make.bat
        ├── Makefile
        └── source
            ├── conf.py
            ├── content
            │   ├── cahier_des_charges.rst
            │   ├── code.rst
            │   ├── objectifs.rst
            │   ├── organisation.rst
            │   ├── postgresql.rst
            │   ├── preinstallation.rst
            │   └── sphinx.rst
            ├── index.rst
            ├── _static
            │   ├── Diagramme_SAE.png
            │   └── not_empty.txt
            └── _templates
                └── not_empty.txt

* ``make.bat`` = fichier bat pour générer la configuration (ne pas utiliser, préférez ``sphinx_build.sh``) depuis Windows

* ``Makefile`` = fichier make pour générer la configuration (ne pas utiliser, préférez ``sphinx_build.sh``) depuis Linux

* ``conf.py`` = fichier de configuration de Sphinx

* ``cahier_des_charges.rst`` = fichier reStrucuredtext parlant du cahier des charges demandés pour ce projet

* ``code.rst`` = fichier reStrucuredtext parlant des modules du programme (utilisant automodule de Sphinx)

* ``objectifs.rst`` = fichier reStrucuredtext parlant des objectifs du projet

* ``organisation.rst`` = fichier reStrucuredtext parlant de l'organisation du projet (vous êtes ici)

* ``postgresql.rst`` = fichier reStrucuredtext parlant de la mise en place de la base de données PostgreSQL

* ``preinstallation.rst`` = fichier reStrucuredtext parlant des modules requis et divers choses à faire avant de lancer le programme principal

* ``sphinx.rst`` = fichier reStrucuredtext parlant de la mise en place de la documentation Sphinx

* ``index.rst`` = fichier reStrucuredtext principal, c'est l'accueil

--------------------------------------------
Organisation des fichiers du dossier ``test``
--------------------------------------------

.. code-block:: bash

    └── test
        ├── dashboard.py
        ├── envoi.py
        ├── graph_test.py
        ├── __init__.py
        ├── new_save.py
        ├── new_send.py
        ├── __pycache__     #dossier de cache, peu intéressant
        │   ├── test.cpython-312.pyc
        │   └── test_psutil.cpython-311.pyc
        ├── save.py
        ├── search.py
        ├── send_json.py
        ├── ssh_interrogateur.py
        ├── tableau_de_bord.py
        ├── test_boucle.py
        ├── test_envoie_BD.py
        ├── test_psutil.py
        └── test.py

* ``dashboard.py`` = 

* ``envoi.py`` = 

* ``graph_test.py`` = 

* ``new_save.py`` = 

* ``new_send.py`` = 

* ``save.py`` = 

* ``search.py`` = 

* ``send_json.py`` = 

* ``ssh_interrogateur.py`` = programme qui nous permettra d'établir une connexion ssh à l'application cliente depuis le panel administrateur, afin de pouvoir modifier le délai d'envoi des données du client vers la base de données

* ``tableau_de_bord.py`` = 

* ``test_boucle.py`` = fichier de test de manipulation de boucle

* ``test_envoie_BD.py`` = fichier de test de l'envoi de données sur la base de données

* ``test_psutil.py`` = fichier de test du module ``psutil``

* ``test.py`` = 

