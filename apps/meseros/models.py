from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    edad = models.CharField(max_length=2, default='18')
    procedencia = models.CharField(max_length=12,default='')



    def __str__(self):
        return "{} de {} y tiene {}".format(self.nombre, self.nacionalidad,self.edad)


