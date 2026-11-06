from django.db import models

# Create your models here.
# se crean tablas 

# construir las migraciones
class Mensaje(models.Model):
    mensaje = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)


    def __str__(self):
        return self.mensaje