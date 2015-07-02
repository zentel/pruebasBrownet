from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	edad = models.IntegerField(default=0)
