# SimpleArrayField Bug (Django)
SimpleArrayField is missing a clean method, this leads to an admin form validation error when a model with a field of the following form is used:
```
ArrayField(models.IntegerField(choices=((0, 'foo'),(1, 'bar'))))
```

## Setup environment:
```
$ sudo apt-get install postgresql-9.4
$ python3 -m venv ~/.dsaf
$ . ~/.dsaf/bin/activate
$ pip install -r requirements.txt
$ createdb -U postgres safd
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Reproduction steps:
* python manage.py runserver
  * Navigate to http://localhost:8000/admin/bug\_app/arrayfieldmodel/add/
  * Enter the integer value 1 and press save.
  * Should see the error message: "Item 0 in the array did not validate:"
* Alternatively run reproducer.py

![alt text](https://github.com/sgallen/django-simplearrayfield-bug/raw/master/SimpleArrayField-admin-error.png "Screenshot of admin error.")

## Extra:
```
from django import forms
from django.contrib.postgres.forms.array import SimpleArrayField
t = forms.TypedChoiceField(choices=((1,'foo'), (2, 'bar')), coerce=int)
field = SimpleArrayField(t)
field.clean('1')
```
