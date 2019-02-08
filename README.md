# Cookiecutter Wagtail Bootstrap, with Heroku/S3 deployment
CWBHSD for short

## Installation

### Create a new project

Run the script in the diretcor you want your project to be store in. eg. ~/Sites

```bash
cookiecutter https://github.com/Designer023/cookiecutter-wagtail-bootstrap-heroku.git
```

**Answer the questions**

```bash
project_name [wagtail_cms_bootstrap_heroku]: Site Name
project_description [My new project is awesome!]: This is project for something!
repo_name [site-name]:
pkg_name [site_name]:
postgres_hostname [localhost]:
postgres_port [5432]:
postgres_database [site_name]:
postgres_user [postgres]:
postgres_password [postgres]:
```

A new project will be created in the ```pkg_name``` directory. ```PKG_NAME``` will be used in the examples below where you need to replace your details. 

### Install locally

**Make sure you are in the package folder**.

```bash
cd PKG_NAME
```

#### Yarn/Node

Install the node packages and build the frontend styles and javascript.

```bash
yarn install
yarn run start
```

#### Pipenv/Python

Install the python dependencies.

```bash
pipenv install
```

#### Database

Create a database with the same name as you setup in the initial questions. This defaults to the same name as your ```PKG_NAME```.

### Setup locally

#### Site admin and management
Make sure the pipenv shell is active, and then migrate the database and create a superuser.
```bash
pipenv shell
python manage.py migrate
python manage.py createsuperuser
```

Run the server
```bash
python manage.py runserver
```

1. Login to admin ```http://127.0.0.1:8000/admin```
2. Create a new root page
3. Settings > sites > edit the exiting localhost to choose the new page as the root
4. Visit ```http://127.0.0.1:8000``` to view your new homepage.

### Setup on Heroku

Heroku deploys from Git.

#### Create a repository

```bash
git init
git add .
git commit -am "A GOOD INITIAL COMMIT MESSAGE"
```

Create the project in Heroku by running the [heroku command line interface](https://devcenter.heroku.com/articles/heroku-cli). All following steps require this to be on your system.

```bash
heroku create
```

This will return one of Heorku's funky named project name.

```bash
https://smooth-pebbles-74623.herokuapp.com/ | https://git.heroku.com/smooth-pebbles-74623.git
```

**OPTIONAL**: You can push this to a GitHub as a new project if you want to. You can change the settings to auto deploy from Github once the project is up and running. For now we will just focus on Heroku git deploys.


#### Configure AWS

The media and static files are hosted on AWS (S3). You will need to create a new bucket and configure the accesskeys and secret keys. The buckets should be publicly viewable. 
You will also need to setup a CORS policy for your new bucket.


##### AWS CORS example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>HTTPS_URL_TO_HEROKU_APP_WITHOUT_TRAILING_SLASH</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
        <AllowedHeader>Content-*</AllowedHeader>
        <AllowedHeader>Host</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

Eg.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>https://smooth-pebbles-74623.herokuapp.com</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
        <AllowedHeader>Content-*</AllowedHeader>
        <AllowedHeader>Host</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

#### Deploy to Heroku

##### Configure buildpacks
Add the Python buildpack then the NodeJS buildpack as the first buildpack
```bash
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku/nodejs
```

##### Configure environmental variables

```bash
# DJANGO SETTINGS
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set DJANGO_SETTINGS_MODULE=PKG_NAME.settings.production
heroku config:set SECRET_KEY=A_SECRET_KEY
heroku config:set SITE_HOST_URL=smooth-pebbles-74623.herokuapp.com

# AWS
heroku config:set AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
heroku config:set AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY
heroku config:set AWS_STORAGE_BUCKET_NAME=BUCKET_NAME 
```

When these are all set you can push the code and it will:
1. Install Node dependencies using Yarn 
2. Install python dependencies using Pipenv
3. Build CSS and JS from the frontend folder in the app
4. Migrate the database
5. Push static files (includeing built files) to AWS

```bash
git push heroku master
```

Once deployed all that remains is to create a super user:

```bash
heroku run python manage.py createsuperuser
```

Then create some initial pages:

1. Login to admin ```https://smooth-pebbles-74623.herokuapp.com/admin```
2. Create a new root page
3. Settings > sites > edit the exiting localhost to choose the new page as the root.
4. Visit: ```https://smooth-pebbles-74623.herokuapp.com``` to view your new homepage.