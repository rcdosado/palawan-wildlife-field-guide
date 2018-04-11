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

    1. `$ python3 -m venv project_msit`
    2. `$ . project_msit/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Set Environment Variables:
	copy local.sample.env at <project_msit>/src/<project_msit>/settings/ as local.env 
	set new SECRET_KEY, and set the database to use, default is sqlite

Run migrations:
    
    python manage.py migrate

Create Admin account:
	python manage.py createsuperuser
	provide information

Run application:
	python manage.py runserver

### Detailed instructions

Take a look at the docs for more information.

[1]: https://www.python.org/
[2]: https://www.djangoproject.com/

# palawan-wildlife-field-guide
Copyleft 2018. 
