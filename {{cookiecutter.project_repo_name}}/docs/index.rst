¡Bienvenido a la documentación de {{ cookiecutter.project_name }}!
======================================

{{ cookiecutter.project_short_description }}

.. toctree::
   :maxdepth: 2

   README.md
   {% if cookiecutter.create_author_file == 'y' -%}authors{% endif -%}
   HISTORY.md

Indices y tablas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
