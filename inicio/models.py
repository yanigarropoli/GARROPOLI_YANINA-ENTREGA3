from django.db import models


# Create your models here

class Vinos (models.Model):
    variedad= models.CharField(max_length=30)
    etiqueta= models.CharField(max_length=30)
    descripcion= models.TextField(null=True, blank=True)
    fecha_creacion = models.DateField(null=True, default=None)
    imagen= models.ImageField(upload_to='imagenes', null=True, blank=True)
    def __str__(self):
        return f" {self.variedad} {self.etiqueta} "


