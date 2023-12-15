=============================================
Documentation Sphinx
=============================================

.. note:: 

    Cette documentation retrace seulement les commandes effectuées pour la partie Sphinx (exemple : création de la documentation, création du site web...).

--------------------------------------------
Installation du programme Sphinx
--------------------------------------------

.. code-block:: bash

    sudo apt-get install python3-sphinx python3-sphinx_rtd_theme

Ou

.. code-block:: bash

    pip install sphinx sphinx-rtd-theme

.. warning::

   Pour les systèmes RPM : python3-sphinx.noarch et python3-sphinx_rtd_theme.noarch

--------------------------------------------
Génération de l'arborescence des répertoires de la documentation
--------------------------------------------

.. code-block:: bash
    
    sphinx-quickstart docs

.. danger::

   À ne faire qu'une seule fois, juste après l'installation !

--------------------------------------------
Finalisation de l'installation
--------------------------------------------

Il faut ajouter la ligne suivante dans le fichier .bashrc du répertoire personnel :

.. code-block:: bash

    export PYTHONPATH=$PYTHONPATH:/chemin_vers_repertoire_module

Dans le fichier de configuration ``source/conf.py`` de sphinx, il faut vérifier que l’extension ``sphinx.ext.autodoc`` est présente, sinon il faut la rajouter :

.. code-block:: bash

    extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    ]

--------------------------------------------
Génération des modules
--------------------------------------------

.. code-block:: bash

    sphinx-apidoc --private -o docs/source/content test

--------------------------------------------
Génération de la documentation
--------------------------------------------

Pour générer la documentation Sphinx, on utilise la commande suivante : 

.. code-block:: bash
    
    sphinx-build docs/source/ html/

- Avec ``docs/source/`` le répertoire où se situe le répertoire principal de la documentation Sphinx
- Et ``html/`` le répertoire de destination où se situera le site web statique

On peut aussi générer la documentation via le script bash suivant :

.. code-block:: bash

    rm -rf html
    mkdir html
    sphinx-build docs/source/ html/
    #firefox -new-tab "html/index.html"

.. note:: 

    Pour lancer automatiquement dans le navigateur Firefox, décochez la dernière ligne

Pour lancer ce script : 

.. code-block:: bash

    chmod +x sphinx-build.sh

Puis

.. code-block:: bash

    ./sphinx-build.sh