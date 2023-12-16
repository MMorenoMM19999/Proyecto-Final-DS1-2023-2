from django.urls import path, re_path
from .forms import CrearCotizacion, ActualizarCotizacion
from .views import ListaCotizaciones, PdfCreateView

urlpatterns = [
    # URL that redirects to the page for creating quotations
    path('cotizacion/crear/', CrearCotizacion.as_view(), name='crear'),
    re_path(r'^cotizacion/(?P<pk>\d+)/$', ActualizarCotizacion.as_view(), name='actualizar'),
    path('cotizacion/listado/', ListaCotizaciones.as_view(), name='listar'),
    re_path(r'^cotizacion/PDF/(?P<pk>\d+)/$', PdfCreateView.as_view(), name='pdf'),
]

