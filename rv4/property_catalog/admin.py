from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Property,Proyect,Images


@admin.register(Property)
class CustomAdminClass(ModelAdmin):
    pass


# Register your models here.
