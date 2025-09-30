from django import forms
from django.contrib.auth.models import User
from caja.models import Caja
from negocio.models import Negocio

class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['monto_inicial', 'turno', 'usuario_apertura']
        labels = {
            'monto_inicial': 'Monto inicial de efectivo'
        }

    def __init__(self, *args, **kwargs):
        negocio = kwargs.pop('negocio', None)
        super(CajaForm, self).__init__(*args, **kwargs)

        if negocio:
            usuarios = User.objects.filter(negocio=negocio)
            self.fields['usuario_apertura'].queryset = usuarios


