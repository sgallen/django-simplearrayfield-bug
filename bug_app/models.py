from django.db import models
from django.contrib.postgres.fields import ArrayField


class ArrayFieldModel(models.Model):
    CHOICES = (
        (1, 'foo'),
        (2, 'bar'),
    )

    arrays = ArrayField(
        models.IntegerField(choices=CHOICES),
        default=list
    )
