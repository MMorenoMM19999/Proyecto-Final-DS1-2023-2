from django.urls import path
from .forms import CrearCliente, ActualizarCliente
from .views import ListaClientes
from .views import ClienteDetailView

urlpatterns = [
    # URL that redirects to the customer creation page
    path('cliente/crear/', CrearCliente.as_view(), name='crear'),
    path('cliente/<int:pk>/', ActualizarCliente.as_view(), name='actualizar'),
    path('cliente/listado/', ListaClientes.as_view(), name='listar'),
    path('cliente/<int:pk>/detalle/', ClienteDetailView.as_view(), name='detalle'),
]
