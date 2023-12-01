#programme pour directement générer le site html
rm -rf html
mkdir html
sphinx-build docs/source/ html/
#firefox -new-tab "html/index.html"