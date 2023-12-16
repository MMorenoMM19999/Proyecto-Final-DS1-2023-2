from django.urls import re_path
from .forms import OrdenDeTrabajoCreateView
from .forms import OrdenDeTrabajoUpdateView
from .views import OrdenDeTrabajoListView
from .views import RetirarEntregarVehiculoTemplateView

urlpatterns = [
    re_path(r'^orden_de_trabajo/crear/$', OrdenDeTrabajoCreateView.as_view(), name='crear'),
    re_path(r'^orden_de_trabajo/(?P<pk>\d+)/$', OrdenDeTrabajoUpdateView.as_view(), name='actualizar'),
    re_path(r'^orden_de_trabajo/listado/', OrdenDeTrabajoListView.as_view(), name='listar'),
    re_path(r'^orden_de_trabajo/retirar/entregar/(?P<pk>\d+)/', RetirarEntregarVehiculoTemplateView.as_view(), name='entregar-retirar-vehiculo')
]

