from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=5, default='30')

    def __str__(self):
        return "{}".format(self.nombre)