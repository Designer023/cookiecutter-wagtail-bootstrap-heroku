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


```bash
heroku create
heroku buildpacks:set heroku/python --app heroku-app-name-12345
heroku buildpacks:add --index 1 heroku/nodejs --app heroku-app-name-12345
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-12345
heroku addons:create heroku-postgresql:hobby-dev --app heroku-app-name-12345
heroku config:set DJANGO_SETTINGS_MODULE=YOUR_APP_NAME.settings.production --app heroku-app-name-12345

SITE_HOST_URL=HEROKU_APP_URL
AWS_ACCESS_KEY_ID=XXXXXXX
AWS_SECRET_ACCESS_KEY=YYYYYYYY
AWS_STORAGE_BUCKET=BUCKET_NAME

```

```

heroku git:remote -a heroku-app-name-12345
git push heroku master

heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --no-input

heroku run python manage.py check --deploy

heroku open
```