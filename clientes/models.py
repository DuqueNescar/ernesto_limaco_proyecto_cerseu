from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, default='00000000')

    def __str__(self):
        return "{} de {}".format(self.nombre, self.apellido)