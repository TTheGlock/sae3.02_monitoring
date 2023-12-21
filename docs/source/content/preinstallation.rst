=============================================
Préinstallation
=============================================

--------------------------------------------
Modules Python
--------------------------------------------

.. warning::

   Ces modules sont vitaux pour le bon fonctionnement des programmes.

.. note:: 

    Vous pouvez retrouver ces modules dans le fichier *requirements.txt*, à la racine du dossier.

* ``psutil`` v5.9.6 ou +
    - via https://pypi.org/project/psutil/
    - ``pip install psutil``
* ``get-mac`` v0.9.2 ou +
    - via https://pypi.org/project/get-mac/
    - ``pip install get-mac``
* ``pyqt6`` v6.6.0 ou +
    - via https://pypi.org/project/PyQt6/
    - ``pip install PyQt6``
* ``sphinx-rtd-theme`` v1.3.0 ou +
    - via https://pypi.org/project/sphinx-rtd-theme/
    - ``pip install sphinx-rtd-theme``
* ``netifaces`` v0.11.0 ou +
    - via https://pypi.org/project/netifaces/
    - ``pip install netifaces``
* ``paramiko`` v3.3.1 ou +
    - via https://pypi.org/project/paramiko/
    - ``pip install paramiko``
* ``psycopg2`` v2.9.9 ou +
    - via https://www.psycopg.org/docs/install.html
    - ``pip install psycopg2-binary``
* ``matplotlib`` v3.8.2 ou +
    - via https://pypi.org/project/matplotlib/
    - ``pip install matplotlib``
* ``PyQtChart`` v5.15.6 ou +
    - via https://pypi.org/project/PyQtChart/
    - ``pip install PyQtChart``
* ``platform`` v1.0.8 ou +
    - déjà installé de base avec python>=3.11
* ``shutil``
    - déjà installé de base avec python>=3.11
* ``socket``
    - déjà installé de base avec python>=3.11
* ``time``
    - déjà installé de base avec python>=3.11   

--------------------------------------------
Ajout du dossier principal au PATH
--------------------------------------------

Dans le fichier `.bashrc` du répertoire personnel, il faut ajouter la ligne suivante : 

``export PYTHONPATH=$PYTHONPATH:/.../sae302-monitoring/sae302-monitoring``

.. warning::

   Il faut préciser le chemin complet dans les "...".
