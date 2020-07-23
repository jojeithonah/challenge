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
* [Deploy AWS Lambda](#deploy-aws-lambda)
* [Variables de entorno](#variables-de-entorno)
* [Postman](#postman)
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
# Asigna permisos al instalador
$ chmod +x installer.sh

# Inicia el instalador
$ bash installer.sh
```

#### Manual

```
# Crea un entorno virtual
$ virtualenv -p python3 venv

# Activa el entorno
$ source venv/bin/activate

# Variables locales
$ cp .env.sample .env

# Modificar variables necesarias
$ nano .env

# Instala los requerimientos
$ pip install -r requeriments.txt
```


## Deploy AWS Elastic Beanstalk en un entorno local
#### Lambda Serverless (usando zappa)
```

```


## Variables de entorno
```
DEBUG=
SECRET_KEY=
APPNAME=
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=5432

```

#### General
```
# Ejecutar migraciones
$ python manage.py migrate

# Ejecutar proyecto
$ python manage.py runserver

# Ejecutar archivos estaticos
$ python manage.py collectstatics
```

## Crear una nueva app dentro del proyecto
```
# Ingresa
$ cd project/apps

# Crear una nueva aplicacion
$ django-admin startapp myappname
```

## Referencias

* [Python](https://www.python.org/doc/)
* [Django](https://docs.djangoproject.com/en/3.0/)

