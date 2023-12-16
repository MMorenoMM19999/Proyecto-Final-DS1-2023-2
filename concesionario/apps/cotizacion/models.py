from django.db import models
from datetime import datetime    
from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo

CREDITO = 'Credito'
EFECTIVO = 'Efectivo'
TARJETA_CREDITO = 'Tarjeta_credito'
TARJETA_DEBITO = 'Tarjeta_debito'

forma_pago_choices = (
    (CREDITO, 'Credito'),
    (EFECTIVO, 'Efectivo'),
    (TARJETA_CREDITO, 'Tarjeta de credito'),
    (TARJETA_DEBITO, 'Tarjeta de debito'),
)

class Cotizacion(models.Model):
    empleado = models.ForeignKey(Empleado, default=None, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, default=None, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, default=None, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    forma_pago = models.CharField(max_length=20, choices=forma_pago_choices, default=EFECTIVO)
    habilitado = models.BooleanField(default=True)

    # Explicitly defining BigAutoField as the primary key
    id = models.BigAutoField(primary_key=True)

    class Meta:
        ordering = ['fecha']
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        return str(self.fecha)

    def __unicode__(self):
        return str(self.fecha)
