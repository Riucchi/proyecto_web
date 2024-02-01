from django import forms
from app_coder.models import Registro

class registro_db(forms.ModelForm):
    class Meta:
        model = Registro
        campos = ['nombre', 'apellido', 'edad', 'hotmail']
        