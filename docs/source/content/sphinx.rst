=============================================
Documentation Sphinx
=============================================

.. note:: 

    Cette documentation retrace seulement les commandes effectuées pour la partie Sphinx (exemple : création de la documentation, création du site web...).

--------------------------------------------
Installation du programme Sphinx
--------------------------------------------

.. code-block:: bash

    sudo apt-get install python3-sphinx python3-sphinx-rtd-theme

.. warning::

   Pour les systèmes RPM : python3-sphinx.noarch et python3-sphinx_rtd_theme.noarch

--------------------------------------------
Génération de l'arborescence des répertoires de la documentation
--------------------------------------------

.. code-block:: bash
    
    sphinx-quickstart docs

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

Pour lancer ce script : 

.. code-block:: bash

    chmod +x sphinx-build.sh
    ./sphinx-build.sh