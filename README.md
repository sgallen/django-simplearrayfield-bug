# django-simplearrayfield-bug
SimpleArrayField is missing a clean method, this leads to an admin form validation error when a model of type ArrayField(models.IntegerField(choices=((0, 'foo'),(1, 'bar')))) is used.
