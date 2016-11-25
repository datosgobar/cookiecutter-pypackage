{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

[![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}?branch=master)
[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }})
[![PyPI](https://badge.fury.io/py/{{ cookiecutter.project_repo_name }}.svg)](http://badge.fury.io/py/{{ cookiecutter.project_repo_name }})
[![Stories in Ready](https://badge.waffle.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}.png?label=ready&title=Ready)](https://waffle.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }})
[![Documentation Status](http://readthedocs.org/projects/{{ cookiecutter.project_repo_name }}/badge/?version=latest)](http://{{ cookiecutter.project_repo_name }}.readthedocs.org/en/latest/?badge=latest)

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Licencia: {{ cookiecutter.open_source_license }}
* Documentación: https://{{ cookiecutter.project_repo_name | replace("_", "-") }}.readthedocs.io
{% endif %}

## Instalación

*AYUDA: ¿Qué dependencias del sistema son necesarias? ¿Tests/pruebas post instalación? Usar screenshots/gifs (si cabe).*

* `cd path/to/{{ cookiecutter.project_repo_name }}` y `pip install -e .` para instalar el repo clonado localmente en *modo developer* (cualquier cambio en el código está disponible en el entorno virtual donde fue instalado).

## Uso

*AYUDA: Ejemplo rápido. Usar screenshots/gifs (si cabe).*

## Tests

*AYUDA: ¿Cómo correr los tests? ¿Cómo me instalo dependencias para los tests?*

## Créditos

*AYUDA: ¿Usás código de otra persona/organización? ¿Alguien o algo fue una fuente de inspiración/asesoramiento/ayuda para este repositorio? ¿Es esto un fork?*

## Contacto

Te invitamos a [crearnos un issue](https://github.com/datosgobar/{{ cookiecutter.project_repo_name }}/issues/new?title=Encontre un bug en {{ cookiecutter.project_repo_name }}) en caso de que encuentres algún bug o tengas feedback de alguna parte de `{{ cookiecutter.project_repo_name }}`.

Para todo lo demás, podés mandarnos tu comentario o consulta a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar).
