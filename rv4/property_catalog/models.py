from django.db import models



class Proyect(models.Model):
    id_external = models.BigIntegerField()
    nombre_proyecto = models.CharField(max_length=255,blank=True,null=True)
    direccion = models.CharField(max_length=255,blank=True,null=True)
    aprobacion12cuotas = models.CharField(max_length=255,blank=True,null=True)
    tipo = models.CharField(max_length=255,blank=True,null=True)
    ubicacion = models.CharField(max_length=255,blank=True,null=True)
    estado = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateField(blank=True,null=True)
    updated_at = models.DateField(blank=True,null=True)
    api = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.nombre_proyecto,self.direccion)
    
    class Meta:
        verbose_name_plural = "Proyectos"

class Property (models.Model):
    external_id = models.BigIntegerField()
    propiedad = models.CharField(max_length=255,blank=True,null=True)
    area = models.IntegerField()
    tipo = models.CharField(max_length=255,blank=True,null=True)
    clase_tipo = models.CharField(max_length=255,blank=True,null=True)
    modelo = models.CharField(max_length=255,blank=True,null=True)
    ubicacion = models.CharField(max_length=255,blank=True,null=True)
    estado = models.CharField(max_length=255,blank=True,null=True)
    fin_de_obra = models.DateField(blank=True,null=True)
    fase = models.CharField(blank=True,null=True)
    bloqueo = models.CharField(blank=True,null=True)
    precio = models.FloatField(blank=True,null=True)
    precio_sugerido = models.FloatField(blank=True,null=True)
    proyecto_id = models.ForeignKey(Proyect,on_delete=models.CASCADE,blank=True,
        null=True)
    habitaciones = models.IntegerField(blank=True,null=True)
    baños = models.IntegerField(blank=True,null=True)
    parqueos = models.IntegerField(blank=True,null=True)
    m2construccion = models.IntegerField(blank=True,null=True)
    largo = models.IntegerField(blank=True,null=True)
    ancho = models.IntegerField(blank=True,null=True)
    año = models.BigIntegerField(blank=True,null=True)
    titulo = models.CharField(max_length=255,blank=True,null=True)
    descripcion = models.TextField(blank=True,null=True)
    detalles = models.CharField(blank=True,null=True)
    descripcion_corta = models.TextField(blank=True,null=True)
    caracteristicas = models.CharField(max_length=255,blank=True,null=True)
    latitud = models.FloatField(blank=True,null=True)
    longitud = models.FloatField(blank=True,null=True)
    comision_referencia = models.FloatField(blank=True,null=True)
    comision_directa = models.FloatField(blank=True,null=True)
    created_at = models.DateField(blank=True,null=True)
    updated_at = models.DateField(blank=True,null=True)
    api = models.BooleanField(default=False)



    def __str__(self):
        return '{} - {}'.format(self.external_id,self.propiedad)
    
    class Meta:
        verbose_name_plural = "Propiedades"


class Images(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255,blank=True,null=True)
    url = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    api = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return '{} - {}'.format(self.property.propiedad,self.tipo)

class Comentario(models.Model):
    propiedad = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)