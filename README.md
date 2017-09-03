Python test project 
==========

Requirements
==========
* python 2.7
* django 1.9
```
    pip install django
```
* django-bootstrap3, can use bootstrap css for html
```
    pip install django-bootstrap3
```
* MySQL-python, install using following link. After installed, run 'import MySQLdb' in python console.
```
    http://www.codegood.com/archives/129
```

Usage
===
* Create table (eg. errorlog)
```
    python manage.py makemigrations errorlog
    python manage.py migrate
```
* Run server, Open URL localhost:8000 in the browser
```
    python manage.py runservre
```

Project Structure
===

Reference
====
* Python : http://www.runoob.com/python/python-tutorial.html
* Django : http://python.usyiyi.cn/translate/django_182/index.html
* Django-bootstrap3 : http://django-bootstrap3.readthedocs.io/