from django.urls import include, path  # Use 'path' instead of 'url'
from .forms import CrearVenta
from .views import ListaVentas
from .views import FacturaCreateView

urlpatterns = [
    # redirecciona a la pagina de creacion de venta
    path('venta/crear/', CrearVenta.as_view(), name='crear'),  # Use 'path' instead of 'url'
    # redirecciona a pagina que despliega el listado de ventas
    path('venta/listado/', ListaVentas.as_view(), name='listar'),  # Use 'path' instead of 'url'
    # factura
    path('venta/factura/<int:pk>/', FacturaCreateView.as_view(), name='factura'),  # Use 'path' instead of 'url'
]
