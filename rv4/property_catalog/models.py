from django.db import models

class Property (models.Model):
    external_id = models.BigIntegerField()
    propiedad = models.CharField(max_length=255)
    area = models.IntegerField()
    tipo = models.CharField(max_length=255)
    clase_tipo = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    fin_de_obra = models.DateField()
    fase = models.CharField()
    bloqueo = models.CharField()
    precio = models.BigIntegerField
    precio_sugerido = models.BigAutoField
    proyecto_id = models.IntegerField()
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    parqueos = models.IntegerField()
    m2construccion = models.IntegerField()
    largo = models.IntegerField()
    ancho = models.IntegerField()
    año = models.BigIntegerField()
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    detalles = models.CharField()
    descripcion_corta = models.TextField()
    caracteristicas = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=6, decimal_places=2)
    longitud = models.DecimalField(max_digits=6, decimal_places=2)
    comision_referencia = models.DecimalField(max_digits=6, decimal_places=2)
    comision_directa = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField()
    updated_at = models.DateField()
    api = models.BooleanField(default=False)


    def __str__(self):
        return '{} - {}'.format(self.external_id,self.propiedad)

class Proyect(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    id_external = models.BigIntegerField()
    nombre_proyecto = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    aprobacion12cuotas = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()



class Images(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
