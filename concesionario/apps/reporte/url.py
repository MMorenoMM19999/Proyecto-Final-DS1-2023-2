# -*- encoding: utf-8 -*-

from django.urls import include, re_path

from .forms import ReporteVendedores
from .forms import ReporteVentasSucursal
from .forms import ReporteGananciasSucursal
from .forms import ReporteVehiculosSucursal
from .forms import ReporteProveedoresUsados
from .forms import ReporteSucursalRepuestos


# Updated URL patterns
urlpatterns = [
    re_path(r'^reporte/MejoresVendedores/$', ReporteVendedores.as_view(), name='MejoresVendedores'),
    re_path(r'^reporte/VentasSucursal/$', ReporteVentasSucursal.as_view(), name='VentasSucursal'),
    re_path(r'^reporte/GananciasSucursal/$', ReporteGananciasSucursal.as_view(), name='GananciasSucursal'),
    re_path(r'^reporte/VehiculosSucursal/$', ReporteVehiculosSucursal.as_view(), name='VehiculosSucursal'),
    re_path(r'^reporte/ProveedoresUsados/$', ReporteProveedoresUsados.as_view(), name='ProveedoresUsados'),
    re_path(r'^reporte/SucursalRepuestos/$', ReporteSucursalRepuestos.as_view(), name='SucursalRepuestos'),
]