from django.http import HttpResponse
from app_coder.models import Registro

def agregar_curso(request):
    registro = Registro(nombre="lucas",apellido="beccarini",edad=26,email="lucasbecca3@hotmail.com")
    registro1 = Registro(nombre="franco",apellido="beccarini",edad=35,email="franco_beca03@hotmail.com")
    registro2 = Registro(nombre="tiziana",apellido="teilleri",edad=23,email="tizianateilleri@gmail.com")
    registro.save()
    registro1.save()
    registro2.save()

    return HttpResponse("carga exitosa")