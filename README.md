# Cookiecutter PyPackage - Datos Argentina

Cookiecutter template para paquetes de Python del equipo de Datos Argentina.

*Nota: Este proyecto recién está comenzando a ser una **idea**, usar con precaución. Todavía deben adaptarse/traducirse varias partes y eliminar algunas cosas que no usamos.*

Esto es un fork del [audrey/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage/) que estamos adaptando y traduciendo para uso de los nuevos repositorios pythonicos del equipo de Datos.

## Features

* Travis-CI: Preparado para integración continua con Travis CI.
* Sphinx docs: Documentación preparada para generar con ReadTheDocs.
* Auto-release a PyPI: Cada vez que se hace un *tag* con una nueva versión, se publica en PyPi automáticamente.

## Instalación

Instalar la última versión de Cookiecutter (este template requiere
Cookiecutter 1.4.0 o mayor)::

    pip install -U cookiecutter

## Uso

1. Crear un repositorio en Github y clonarlo localmente
2. `cookiecutter https://github.com/datosgobar/cookiecutter-pypackage-ar.git` para crear estructura del repo. Mover todo el contenido a la carpeta del repo clonado.
2. `pip install -r requirements_dev.txt` para instalar las dependencias de desarrollo (se recomienda crear un entorno virtual para el proyecto primero)
3. Ir a tu cuenta de Travis CI y agregar este repo (*switch on*)
4. `make pypi` para registrar el repo en Pip y activar el auto-deploy con tags en Travis CI (requiere una cuenta en PyPi). `make pypi` simplemente hace esto:
  - `python setup.py register`
  - `python travis_pypi_setup.py`
5. Agregar el repo a tu cuenta de ReadTheDocs y *switch on* para activar el servicio.
  - `make docs` te permite crear la documentación localmente, para ver cómo queda antes de pushear.

*TODO: Probar instrucciones para auto-deploy de la documentación en un hosting de ReadTheDocs*

Para más detalles ver [cookiecutter-pypackage tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).

## Otros cookiecutter templates para python

Ver repositorio de [audrey/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage/) para otros templates de repos en python o directamente el de [audreyr/cookiecutter](https://github.com/audreyr/cookiecutter) para una lista de templates de todo tipo.

## Créditos

* @audrey por su fantástico *ultimate template* para un repositorio modelo en Python [audrey/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage/).

## Contacto

Te invitamos a [crearnos un issue](https://github.com/datosgobar/{{ cookiecutter.project_repo_name }}/issues/new?title=Encontre un bug en {{ cookiecutter.project_repo_name }}) en caso de que encuentres algún bug o tengas feedback de alguna parte de `{{ cookiecutter.project_repo_name }}`.

Para todo lo demás, podés mandarnos tu comentario o consulta a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar).
