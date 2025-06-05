from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Appointments
from .forms import AppointmentsForm
from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import TextFilter
from django.core.validators import EMPTY_VALUES
# Register your models here.

class FilterStatus(TextFilter):
    title = _("Estatus")
    parameter_name = "Estatus"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(status=self.value())

        return queryset

class FilterCliente(TextFilter):
    title = _("Cliente")
    parameter_name = "Cliente"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(nombre_cliente=self.value())

        return queryset
    

class FilterTelefono(TextFilter):
    title = _("Telefono")
    parameter_name = "Telefono"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(telefono=self.value())

        return queryset
    
class FilterEmail(TextFilter):
    title = _("Telefono")
    parameter_name = "Telefono"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(email=self.value())

        return queryset



@admin.register(Appointments)
class ApointmentsAdminClass(ModelAdmin):
    form = AppointmentsForm
    list_filter_submit = True 
    list_filter = [FilterCliente,FilterTelefono,FilterEmail]

    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Show all objects for superusers
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Retornar una versión del form que tenga el request
        class FormWithRequest(form):
            def __new__(cls, *args, **kwargs_inner):
                kwargs_inner['request'] = request
                return form(*args, **kwargs_inner)
        return FormWithRequest
