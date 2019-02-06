# Cookiecutter Django Wagtail with Boostrap for Heroku

## Install

```bash
cookiecutter THIS_REPO_OR_PATH_TO_FOLDER_ON_MACHINE
```

*Answer the questions*
```bash
project_name [wagtail_cms_bootstrap_heroku]: Site Name
repo_name [site-name]:
pkg_name [site_name]:
postgres_hostname [localhost]:
postgres_port [5432]:
postgres_database [site_name]:
postgres_user [postgres]:
postgres_password [postgres]:
```

Create a database with the same name/user as you setup. Default is the same as the pkg_name. pkg_name is the name with spaces replaced with _.

```bash
cd new_folder_path
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver [localhost:port]

```

## Heroku install
**Note: these instructions are not custom yet. Taken from the excellent cookiecuuter django project**
```
heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
heroku addons:create heroku-postgresql:hobby-dev
### On Windows use double quotes for the time zone, e.g.
### heroku pg:backups schedule --at "02:00 America/Los_Angeles" DATABASE_URL
heroku pg:backups schedule --at '02:00 America/Los_Angeles' DATABASE_URL
heroku pg:promote DATABASE_URL

heroku addons:create heroku-redis:hobby-dev

heroku addons:create sentry:f1

heroku config:set PYTHONHASHSEED=random

heroku config:set WEB_CONCURRENCY=4

heroku config:set DJANGO_DEBUG=False
heroku config:set DJANGO_SETTINGS_MODULE=pkg_name.settings.production
heroku config:set DJANGO_SECRET_KEY="$(openssl rand -base64 64)"

### Set this to your Heroku app url, e.g. 'bionic-beaver-28392.herokuapp.com'
heroku config:set DJANGO_ALLOWED_HOSTS=

### Assign with AWS_ACCESS_KEY_ID
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=

### Assign with AWS_SECRET_ACCESS_KEY
heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=

### Assign with AWS_STORAGE_BUCKET_NAME
heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=

git push heroku master

heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --no-input

heroku run python manage.py check --deploy

heroku open
```