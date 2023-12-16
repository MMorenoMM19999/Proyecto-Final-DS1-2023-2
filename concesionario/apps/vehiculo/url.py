# -*- encoding: utf-8 -*-

from django.urls import include, path

from .forms import VehiculoCreateView
from .forms import VehiculoUpdateView
from .views import VehiculosListView

from .forms import VehiculoSucursalAjaxCreateView
from .forms import VehiculoSucursalAjaxUpdateView
from .views import VehiculoSucursalListView

from .views import VehiculosListSucursal

urlpatterns = [
    path('vehiculo/crear', VehiculoCreateView.as_view(), name='crear'),
    path('vehiculo/<int:pk>/', VehiculoUpdateView.as_view(), name='actualizar'),
    path('vehiculos/', VehiculosListView.as_view(), name='listar-vehiculos'),

    path('vehiculos/sucursal/<int:spk>/agregar/<int:vpk>/', VehiculoSucursalAjaxCreateView.as_view(), name='agregar-vehiculo-sucursal'),
    path('vehiculos/sucursal/actualizar/<int:pk>/', VehiculoSucursalAjaxUpdateView.as_view(), name='actualizar-vehiculo-sucursal'),
    path('vehiculos/sucursal/<int:pk>/', VehiculoSucursalListView.as_view(), name='listar-vehiculos-sucursal'),

    path('vehiculos/inventario', VehiculosListSucursal.as_view(), name='listar-vehiculos-inventario'),
]

