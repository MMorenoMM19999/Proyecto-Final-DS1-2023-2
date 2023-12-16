from django.urls import re_path
from .forms import CotizacionOrdenDeTrabajoCreateView
from .forms import CotizacionOrdenDeTrabajoUpdateView
from .views import CotizacionOrdenDeTrabajoDetailView
from .views import CotizacionOrdenDeTrabajoListView

urlpatterns = [
    re_path(r'^cotizacion/orden_de_trabajo/crear/(?P<opk>\d+)/$', CotizacionOrdenDeTrabajoCreateView.as_view(), name='crear'),
    re_path(r'^cotizacion/orden_de_trabajo/actualizar/(?P<pk>\d+)/$', CotizacionOrdenDeTrabajoUpdateView.as_view(), name='actualizar'),
    re_path(r'^cotizacion/orden_de_trabajo/detalle/(?P<pk>\d+)/$', CotizacionOrdenDeTrabajoDetailView.as_view(), name='detalle'),
    re_path(r'^cotizaciones/sucursal/(?P<pk>\d+)/$', CotizacionOrdenDeTrabajoListView.as_view(), name='listar'),
]
