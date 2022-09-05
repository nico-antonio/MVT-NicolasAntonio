from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_de_nacimiento=models.DateField()
    relacion=models.CharField(max_length=50)
