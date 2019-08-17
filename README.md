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
    * `wgsi.py`: bridge from web app to web server (normmally not modify)
    



