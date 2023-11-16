import os
import sys

sys.path.insert(0, os.path.abspath('../../sae3.02_monitoring/sae3.02_monitoring'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SAE 3.02 - Monitoring'
copyright = '2023, LECHEVALLIER-COUSSOT Maxence, CECOTTI Enzo, ROUSSELOT Colin, HOUNGBO Charbel, BA Abdourahmane'
author = 'LECHEVALLIER-COUSSOT Maxence, CECOTTI Enzo, ROUSSELOT Colin, HOUNGBO Charbel, BA Abdourahmane'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'sphinx.ext.todo',
'sphinx.ext.mathjax',
'sphinx.ext.ifconfig',
'sphinx.ext.autodoc',
'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
