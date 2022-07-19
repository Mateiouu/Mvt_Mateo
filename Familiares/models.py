from django.db import models
from django.forms import CharField, DateTimeField, IntegerField

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()
    nacimiento = models.DateField()
