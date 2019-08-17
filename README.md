# Web app - Learning Log

## 1. Setup
#### 1.1 create a virtual environment

`virtual environment` : a place on your system where you can install packages 
 and isolated them from other Python packages.
 
create a directory for project (learning_log), switch to that directory in terminal.
 
```
learning_log$ python -m venv ll_env
learning_log$
```

#### 1.2 Activate the virtual environment

activate the virtual environment with the following command:

* Windows

```
learning_log$ ll_env\scripts\activate
(ll_env)learning_log$
```

* Ubuntu

```
learning_log$ source ll_env/bin/activate
(ll_env)learning_log$ 
```

deactivate the virtual environment:
```
(ll_env)learning_log$ deactivate
learning_log$
```

#### 1.3 Install Django
```angular2html
(ll_env)learning$ pip install Django
(ll_env)learning_log$
```

Now we have installed Django in our virtual environment. It will be available only when 
environment is active.

#### 1.4 Create a project in Django
```angular2html
(ll_env)learning_log$ django-admin.py startproject learning_log .
```

**Notes**: on my computer, using command:
```angular2html
django-admin startproject learning_log .
```

system will create a standard structure under learning_log folder:

* `manage.py` : run a default site

* **Django Project** : 
    * `__int__.py`: empty file, identify this is a python package
    * `settings.py`: settings and configurations, `secret_keys`, `debug`, `installed_apps`, `database`, etc.
    * `urls.py`: mapping urls for our site
    * `wgsi.py`: bridge from web app to web server (normmally not modify), acronym for web server gateway interface


1.5 Create database

```angular2html
(ll_env)learning_log$ python manage.py migrate
```

#### 1.6 Run server

run server to get the default website
```angular2html
run $ python manage.py runserver
```

## 2. Staring an App
#### 2.1 start an app
-- a Django project is a group of individual apps that work together to make the project work as a whole.

```angular2html
learning_log$ python manage.py startapp learning_logs
```

`startapp` will create the infrastructure needed to build ann app.


* `models.py`: define the data we want to manage in our app.

#### 2.2 Defining Models
    
> Our data: each user will create a number of topis. Each entry will tie to a topic, and these entries will be displayed as text.
> Each entry will display the timestamp when it was created.

define `model.py`

* Class `Topic`  
which inherits from class `Model` *(a parent class included in Django that 
define the basic functions of our model)*.

    Two **attribute**: `text` and `date_added`
    * `text`: **CharField**, store topic name.*(When we want to store a small amount of text.)*
        * `max_length=200`: When we define a CharField attribute, we have to tell Django how much space it should reserve in the database.

    * `data_added`: DateTimeField, store date and time when we create topic.
        * `auto_add_now=True`: let Django set this attribute to the current date and time automatically.
    
    One **method**: `__str__(self)`
    * `__str__(self)`: display a simple representation of a model. Return the string stored in the `text`.
   
#### 2.3 Activating Models
