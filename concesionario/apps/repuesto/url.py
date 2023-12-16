from django.urls import path, include, re_path
from .forms import CrearRepuesto
from .forms import ActualizarRepuesto
from .views import RepuestosSucursalListView
from .views import RepuestosListView

from .forms import RepuestoSucursalAjaxCreateView
from .forms import RepuestoSucursalAjaxUpdateView
from .views import RepuestoSucursalListView

urlpatterns = [
    path('repuesto/crear', CrearRepuesto.as_view(), name='crear'),
    re_path(r'^repuesto/(?P<pk>\d+)/$', ActualizarRepuesto.as_view(), name='actualizar'),
    path('repuestos/', RepuestosListView.as_view(), name='listar'),

    path('repuestos/sucursal/<int:spk>/agregar/<int:rpk>/', RepuestoSucursalAjaxCreateView.as_view(), name='agregar-repuesto-sucursal'),
    re_path(r'^repuestos/sucursal/actualizar/(?P<pk>\d+)/$', RepuestoSucursalAjaxUpdateView.as_view(), name='actualizar-repuesto-sucursal'),
    path('repuestos/sucursal/<int:pk>/', RepuestoSucursalListView.as_view(), name='listar-repuestos-sucursal'),
]
