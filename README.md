# palawan-wildlife-field-guide

Palawan Wildlife Field Guide is made as a _project for MSIT_. It is built with [Python][1] using the [Django Web Framework][2].

This project has the following basic apps:

* Species (This app, allows you to view Critically Endangered Species in Palawan )
* Profile (Users Profile Page)
* accounts (User's Account page)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv env`
    2. `$ /env/scripts/activate`
    3. `you'll see something like (env) as prefix for your working directory`

Install all dependencies:

    pip install -r requirements.txt

Set Environment Variables:
	1. copy local.sample.env at <project_msit>/src/<project_msit>/settings/ as local.env 
	2. set new SECRET_KEY, you can generate at this site https://www.miniwebtool.com/django-secret-key-generator/
	3. set the database to use if you do not prefer sqlite

Run migrations:
    
    python manage.py migrate

Create Admin account:
	python manage.py createsuperuser
	provide information username, email, password

Run application:
	python manage.py runserver

### Detailed instructions

Take a look at the docs for more information.

[1]: https://www.python.org/
[2]: https://www.djangoproject.com/

# palawan-wildlife-field-guide

Copyleft 2018. 
