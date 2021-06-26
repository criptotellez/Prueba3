from django import forms
from django.forms import ModelForm
from .models import Denuncia

class DenunciaForm(ModelForm):
    class Meta:
        model= Denuncia
        fields = ['idDenuncia','descripcionDenuncia','fechaDenuncia','categoria']