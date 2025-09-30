from django.db import models
from django.contrib.auth.models import User
from negocio.models import Negocio 

# Create your models here.

class Caja(models.Model):
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    hora_creacion = models.TimeField(auto_now_add=True)
    hora_cierre = models.TimeField(auto_now_add=True, null=True, blank=True)

    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    estado = models.CharField(
        max_length=10,
        choices=[ 
            ('Abierta','Abierta'),
            ('Cerrada','Cerrada'),
        ]
    )

    turno = models.CharField(
        max_length=12,
        choices=[ 
            ('Mañana','Mañana'),
            ('Tarde','Tarde'),
        ]
    )

    usuario_apertura = models.ForeignKey(User, related_name='caja_apertura', on_delete=models.CASCADE)
    usuario_cierre = models.ForeignKey(User, related_name='caja_cierre', null=True, blank=True, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)