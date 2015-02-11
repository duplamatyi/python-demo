# Python Demo

## Used techonlogies

 - Ubuntu 14.04.1 LTS
 - Python 2.7
 - Django 1.7
 - PostgreSQL
 - SQLite (test settings: src/settings/test_settings.py)
 - FE libraries managed by django-bower: typeahead.js, underscore, jquery, bootstrap
 - django-nose and selenium used for testing
 - supervisord for daemonizing gunicorn and celery
 - gunicorn workers for WSGI protocol
 - celery for scheduling the daily import
 - for full list of the used Python packages see the src/requirements/common.txt


## Install instrurctions

Create and activate a virtualenv and install the Python requirements.

```
pip install -r src/requirements/dev.txt
```


Create a secret key, complete your local settings and create the shell script for activating your environment.

```
python -c 'import random; import string; print "".join([random.SystemRandom().choice(string.digits + string.letters) for i in range(100)])'
cp dist/local.json.dist dist/local.json
j2 dist/templates/env_start.sh.j2 dist/local.json > bin/env_start.sh
```

Activate your environment

```
source bin/env_start.sh
```

Install the bower components:

```
python manage.py bower install
```

Install yuglify with npm.

```
sudo npm -g install yuglify
```

## Running the tests

Before running the tests collect the static files as the tests run in production mode.

```
python manage.py collectstatic --noinput
```

Running the tests with nose's test runner. (Selenium is set to use Firefox so make sure you have installed it.)

```
python manage.py test --settings=src.settings.test_settings --with-coverage --cover-package=src.apps.hotel --cover-html
```

## Running the development server

```
python manage.py runserver
```

## Using supervisord

Starting the supervisor deamon that manages the gunicorn workers, celery beat and the celery workers.

```
supervisord -c etc/supervisord.conf
```

## Import management command

```
python manage.py import data/city.csv city
python manage.py import data/hotel.csv hotel
```
