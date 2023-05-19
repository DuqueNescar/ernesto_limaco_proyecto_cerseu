from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    edad = models.CharField(max_length=2, default='18')

    def __str__(self):
        return "{} de {}".format(self.nombre, self.nacionalidad)