from django.db import models

# Create your models here.

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    num_tarjeta = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="personas")

    def __str__(self):
        return f"{self.nombre} {self.num_tarjeta}" 