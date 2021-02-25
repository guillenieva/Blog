from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=254)
    imagen = models.ImageField(max_length=100, upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo