# SimpleArrayField Bug (Django)
SimpleArrayField is missing a clean method, this leads to an admin form validation error when a model of type ArrayField(models.IntegerField(choices=((0, 'foo'),(1, 'bar')))) is used.

## Assumptions:
* running Ubuntu 15.10

## Setup environment:
* sudo apt-get install postgresql-9.4
* python3 -m venv ~/.dsaf
* . ~/.dsaf/bin/activate
* pip install -r requirements.txt
* createdb -U postgres safd
* python manage.py migrate
* python manage.py createsuperuser

## Reproduction steps:
* python manage.py runserver
* Navigate to http://localhost:8000/admin/bug_app/arrayfieldmodel/add/
** Enter the integer value 1 and press save.
** Should see the error message: "Item 0 in the array did not validate:"

## Extra:
t = forms.TypedChoiceField(choices=((1,'foo'), (2, 'bar')), coerce=forms.IntegerField.to_python)
field = SAF(t)
field.clean('1')
