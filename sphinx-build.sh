#programme pour directement générer le site html

#suppression de l'ancien répertoire
rm -rf html

#création du répertoire
mkdir html

#géneration de la documentation
sphinx-build docs/source/ html/

#ouverture de la page principale de la documentation dans firefox
firefox -new-tab "html/index.html"