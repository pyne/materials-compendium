# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime
from importlib.metadata import version as metadata_version

# General information about the project.
project = "Materials Compendium"
copyright = "2011-{0}, The PyNE Development Team".format(datetime.datetime.now().year)
author = "PyNE"
release = metadata_version("materials_compendium")
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
    "sphinx_autodoc_typehints",
    "sphinx_design",
    "nbsphinx",
    "myst_nb",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "cloud"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ["_static"]
html_style = "pyne.css"

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# pygments_style = 'friendly'
# pygments_style = 'bw'
# pygments_style = 'fruity'
# pygments_style = 'manni'
pygments_style = "tango"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "sidebarbgcolor": "#F5FAEB",
    "sidebartextcolor": "#864907",
    "sidebarlinkcolor": "#4b1a07",
    #'sidebartrimcolor': '#504A4B',
    "sidebartrimcolor": "#556B2F",
    "collapsiblesidebar": True,
    "stickysidebar": False,
    "relbarbgcolor": "#98bc8c",
    "footerbgcolor": "#fffffff",
    "footertextcolor": "#323039",
    "linkcolor": "#A92727",
    "textcolor": "#323039",
    #'sectionbgcolor': '#EBFAD7',
    "sectionbgcolor": "#F2E3C2",
    "sectiontextcolor": "#0000000",
    "sectiontrimcolor": "#fffffff",
    #'codebgcolor': '#BBCBB6',
    "codebgcolor": "#F8FFE3",
    "codetextcolor": "#000000",
    "min_height": "bottom",
    "googleanalytics_id": "UA-37452818-1",
    "highlighttoc": False,
    "bgcolor": "#ffffff",
    "max_width": "1250px",
    "sidebarwidth": "280px",
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None
html_title = "{project} {release}".format(project=project, release=release)

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None
html_short_title = "{project}".format(project=project)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/pyne_icon_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/pyne_icon.ico"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "pynedoc"
