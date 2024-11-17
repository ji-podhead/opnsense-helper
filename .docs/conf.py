import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Source code dir relative to this file

extensions = [
    'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables
'myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
autosummary_generate = True  # Turn on sphinx.ext.autosummary

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# html_theme = 'alabaster'
# html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "rightsidebar": "true",
    "relbarbgcolor": "black"
}

project = 'opnsense_helper'
copyright = '2024, ji-podhead'
author = 'ji-podhead'
release = '0.1.26'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usa<ge/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

