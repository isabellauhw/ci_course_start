import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # Optional: adds the current directory to Python's import path

# -- Project information -----------------------------------------------------

project = 'My Project'
author = 'Isabel Lau'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Automatically include documentation from docstrings
    'sphinx.ext.napoleon',  # Supports Google and NumPy style docstrings
    'sphinx.ext.viewcode',  # Adds links to the source code
]

templates_path = ['_templates']  # Path to custom HTML templates

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']  # Excludes certain files and folders

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Choose a theme (e.g., 'alabaster', 'sphinx_rtd_theme')
html_static_path = ['_static']  # Path to custom static files (e.g., CSS)

# -- Options for autodoc extension -------------------------------------------

# Optional settings if using autodoc to document Python code
autodoc_member_order = 'bysource'  # Order members by source order
autodoc_default_options = {
    'members': True,  # Include class members
    'undoc-members': True,  # Include members without docstrings
}
