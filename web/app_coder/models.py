from django.db import models
from django import forms

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.CharField(max_length=20)
    def __str__(self):
        return f"nombre : {self.nombre} | apellido: {self.apellido} | edad: {self.edad}, email: {self.email} "

