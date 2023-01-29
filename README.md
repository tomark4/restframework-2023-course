# Django - Django rest framework curso

Curso de repaso de tecnologias:

- Django
- Django rest framework

Instalar pip3

`$sudo apt install python3-pip`

### Run pipenv and test instalation

python -m pipenv --help

para ejecutar en entornos ubuntu / mint es

python -m pipenv [commands]

para que funcione se puede agregar una alias en .bashrc

`$ alias pipenv='python3 -m pipenv'`

### Manejo de pipenv

```
# Crear el entorno virtual

pipenv --python 3.7

# Ver la ubicacion del entorno virtual

pipenv --venv

# Ver la ruta del ejecutable de python

pipenv --py

# Usar el interprete de python del entorno virtual

pipenv run python

# Ver los paquetes instalados en el entorno virtual

pipenv graph

# o como alternativa

pipenv run pip list

# Instalar un paquete

pipenv install [package_name]

# o con pip dentro del virtual env

pipenv run pip install [package_name]

# Desinstalar un paquete

pipenv uninstall [package_name]

# o con pip dentro del virtual env

pipenv run pip uninstall [package_name]

# borrar el entorno virtual

pipenv --rm

# activar el entorno virtual

pipenv shell
```

# vs code configuration

```
{
    "python.pythonPath": "C:\\ruta\\al\\entorno\\python.exe",   /* Adaptar esta línea */
    "python.linting.enabled": true,
    "python.linting.pylintPath": "pylint",
    "python.linting.pylintEnabled": false,
    "python.languageServer": "Pylance",
    "python.linting.pycodestyleEnabled": true,
    "python.analysis.useImportHeuristic": true,
    "python.linting.pycodestyleArgs": ["--ignore=E501,E226,E116"],
    "python.formatting.autopep8Args": ["--max-line-length=200"],
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--disable=django-not-configured,missing-module-docstring,missing-class-docstring"
    ]
}
```
