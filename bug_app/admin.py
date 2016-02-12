from django.contrib import admin

from .models import ArrayFieldModel


class ArrayFieldModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArrayFieldModel, ArrayFieldModelAdmin)
