from django.db import models
from django import forms

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.CharField(max_length=20)



class registro_db(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'edad', 'email']