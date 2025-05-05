# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EduLink 教程'
copyright = '2025, 肖梓航&孙轲俊'
author = '肖梓航'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'EduLink': ('https://edulink.ryanincn11.top/', None),
    '班讯': ('https://classages.edulink.ryanincn11.top/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "furo"
html_title = f"EduLink教程"
html_logo = "images/icon.png"
# -- Options for EPUB output
epub_show_urls = 'footnote'
