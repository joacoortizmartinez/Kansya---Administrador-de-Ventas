from django import forms
from django.contrib.auth.models import User
from .models import Negocio

class NegocioForm(forms.ModelForm):
    class Meta:
        model = Negocio
        fields = ["nombre"]

