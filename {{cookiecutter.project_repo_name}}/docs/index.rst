Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 2

   README.md
   installation
   usage
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors{% endif -%}
   HISTORY.md

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
