from django.db import models
from caja.models import Caja
from django.contrib.auth.models import User

# Create your models here.

class Informe(models.Model):
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    usuario_cierre = models.ForeignKey(User, on_delete=models.CASCADE)
    inicio_hoy = models.DecimalField(max_digits=15, decimal_places=2)
    inicio_mañana = models.DecimalField(max_digits=15, decimal_places=2)

    ventas_efectivo = models.DecimalField(max_digits=15, decimal_places=2)
    ventas_tarjeta = models.DecimalField(max_digits=15, decimal_places=2)
    ventas_dni = models.DecimalField(max_digits=15, decimal_places=2)
    ventas_bna = models.DecimalField(max_digits=15, decimal_places=2)

    total_salidas = models.DecimalField(max_digits=15, decimal_places=2)
    total_retiro = models.DecimalField(max_digits=15, decimal_places=2)
    total_anulado = models.DecimalField(max_digits=15, decimal_places=2)
    
    total = models.DecimalField(max_digits=15, decimal_places=2)