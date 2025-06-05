from .models import Appointments
from django import forms
from django.contrib.auth.models import User


class AppointmentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super().__init__(*args, **kwargs)
    class Meta:
        model = Appointments
        exclude = ['user']

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = User.objects.get(id=self.request.user.id)
        if commit:
            instance.save()
        return instance
