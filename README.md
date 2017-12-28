# isfrost-django - A django project for the isfrost web page

## How to setup
* Create a new virtual environment, activate it
* install requirements with `pip install -r requirements.txt`
* Create a PSQL DB and add in the required parameters for either the development or production environment
* Create a AWS account and create a new bucket as well as a role with full access to read/write on that bucket and add in those required parameters


## How to run
Choose an environment with `DJANGO_SETTINGS_MODULE` set to either
* `isfrost_project.settings.development`
* `isfrost_project.settings.production`
*  start the Django server with `python manage.py runserver`

## Heroku related
Sync with heroku:
* pip freeze > requirements.txt
* git push heroku master
* heroku run python migrate