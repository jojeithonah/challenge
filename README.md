Challenge test
========================================

> Framework [Django 3.0.8](https://docs.djangoproject.com/en/3.0/)

## Documentación

* [Acerca](#acerca)
* [Requisitos](#requisitos)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Instalación](#instalacion)
    - [Instalación Local](#local)
* [Interactivo](#interactivo)
* [Deploy AWS Elastic Beanstalk](deploy-aws-elastic-beanstalk)
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

> Agregar los datos locales de postgresql local
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'prueba',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }

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

#### Deploy AWS Elastic Beanstalk
#### (usando Elastic Beanstalk)

#### (REUISITOS PREVIOS)

```
# pip install awsebcli
# AWS CLI
# CREDENCIALES AWS (ID ACCESO, SECRET)

$eb init 
$ Select an application to use
$ 1) clallenge
$ 2) [ Create new Application ]
$ (default is 2): 2
$ Enter Application Name
$ (default is "challenge-dev"): 
$ Application my_eb_site has been created.
$ It appears you are using Python. Is this correct?(y/n): y

$Select a platform version.
$ 1) Python 3.7
$ 2) Python 3.6
$ 4) Python 3.4 (Preconfigured - Docker)
$ (default is 1): 2

$ Do you want to set up SSH for your instances?
$ (y/n): y

$ Select a keypair.
$ 1) aws-eb
$ 2) [ Create new KeyPair ]
$ (default is 2): 1

$eb create --scale 1 -db -db.engine postgres -db.i db.t2.micro
$ Select a load balancer type
$ 1) classic
$ 2) application
$ (default is 1):

$ Enter an RDS DB username (default is "ebroot"): 
$ Enter an RDS DB master password: 
$ Retype password to confirm:

$ eb deploy


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

## API`s
#POST
- curl -d '{"products": [{"id":"ID1","name":"product","value": 122,"discount_value":0,"stock":1},{"id":"123","name":"product","value":123,"discount_value":0,"stock":1}]}' -H "Content-Type: application/json" -X POST http://testing-dev.us-west-2.elasticbeanstalk.com/api/products/bulk_insert

#GET
- curl -H "Content-Type: application/json" -X GET http://testing-dev.us-west-2.elasticbeanstalk.com/api/products


* [Python](https://www.python.org/doc/)
* [Django](https://docs.djangoproject.com/en/3.0/)

