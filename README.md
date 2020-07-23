Challenge test
========================================

> Framework [Django 3.0.8](https://docs.djangoproject.com/en/3.0/)

## Documentación

* [Acerca](#acerca)
* [Requisitos](#requisitos)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Instalación](#instalacion)
    - [Instalación Local](#local)
* [Crear una nueva app](#crear-una-nueva-app)
* [Referencias](#referencias)

## Acerca

Template inicial con las funcionalidades básicas para el desarrollo de un proyecto basado en el Framework Django


## Requisitos

- virtualenv
- Python 3.6.6
- pip
- (PostgreSQL) 11.12

## Estructura del proyecto
> Esta es la estructura básica del boilerplate.

```
venv/
    ... source files

challenge/
    __init__.py
    apps/
        products/
        ... more apps add here
    urls.py
    wsgi.py
    asgi.py
    settings.py
.env.sample
manage.py
requeriments.txt
```
## Instalación
> Se deben instalar los requisitos mencionados anteriormente.
> En caso que la instalación de los paquetes falle, tomarse en cuenta el siguiente paquete

```
Ubuntu
sudo apt-get install libpq-dev python-dev
pip install setuptools

```

```
# Descargar o Clonar
$ https://github.com/jojeithonah/challenge.git
```

## Deploy Local
#### Maquina virtual o localhost
> Las configuraciones pueden variar dependiendo del sistema operativo

#### Interactivo
```
# Crea un entorno virtual
$ virtualenv -p python3 venv

# Activa el entorno
$ source venv/bin/activate

# Instala los requerimientos
$ pip install -r requeriments.txt

# Migrar
$ python manage.py migrate

# Crear superuser
$ python manage.py createsuperuser

# Run server
$ python manage.py runserver 0.0.0.0:8000
```

## Deploy AWS Elastic Beanstalk en un entorno local
#### Lambda Serverless (usando zappa)
```

```

#### General
```
# Ejecutar archivos estaticos
$ python manage.py collectstatics
```

## Crear una nueva app dentro del proyecto
```

# Crear una nueva aplicacion
$ django-admin startapp myappname
```

## Referencias

* [Python](https://www.python.org/doc/)
* [Django](https://docs.djangoproject.com/en/3.0/)

