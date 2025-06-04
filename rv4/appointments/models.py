from django.db import models
from django.contrib.auth.models import User
from property_catalog.models import Property

STATUS_APPOINTMENT = [
    ("pendiente","PENDIENTE"),
    ("confirmada","CONFIRMADA"),
    ("cancelada","CANCELADA")
]


class Appointments(models.Model):
    fecha = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_APPOINTMENT,
        default="pendiente"
    )
    nombre_cliente = models.CharField(max_length=255)
    telefono = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    notas = models.TextField()
    property = models.ForeignKey(Property,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.nombre_cliente,self.status)