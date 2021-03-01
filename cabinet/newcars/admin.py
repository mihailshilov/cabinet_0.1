from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from newcars.models import NewCar

# admin.site.register(NewCar)


@admin.register(NewCar)
class NewCarAdmin(ModelAdmin):
    pass
