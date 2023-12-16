from django.db import models
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.repuesto.models import Repuesto
from datetime import datetime

class CotizacionOrdenDeTrabajo(models.Model):
    id = models.BigAutoField(primary_key=True)
    orden_de_trabajo = models.OneToOneField(OrdenDeTrabajo, related_name='cotizacion', default='', on_delete=models.CASCADE)
    costo_reparacion = models.FloatField()
    fecha_vencimiento = models.DateField()
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ['fecha_vencimiento']
        verbose_name_plural = "Cotizaciones Ordenes de Trabajo"

    def __str__(self):
        return "Cotizacion {}".format(self.id)

    def __unicode__(self):
        return u"Cotizacion {}".format(self.id)

    def es_valida(self):
        if datetime.now().date() > self.fecha_vencimiento:
            return False
        return True

    def costo_repuestos(self):
        costo_repuestos = 0
        for repuesto_cantidad in self.repuestos_cantidad.all():
            costo_repuestos += (repuesto_cantidad.repuesto.precio * repuesto_cantidad.cantidad)
        return costo_repuestos

    def costo_total(self):
        return self.costo_reparacion + self.costo_repuestos()


class RepuestoCantidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    cotizacion_orden_de_trabajo = models.ForeignKey(CotizacionOrdenDeTrabajo, related_name='repuestos_cantidad',  on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, default='', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name_plural = "Repuestos Cantidad"
        unique_together = (("cotizacion_orden_de_trabajo", "repuesto"),)
