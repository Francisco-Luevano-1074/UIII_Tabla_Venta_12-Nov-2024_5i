from django.db import models

# Create your views here.

class Cliente(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    no_telefono=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    orden=models.CharField(max_length=100)
    mesa=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
