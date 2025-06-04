from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Appointments
# Register your models here.


@admin.register(Appointments)
class ApointmentsAdminClass(ModelAdmin):
    pass
