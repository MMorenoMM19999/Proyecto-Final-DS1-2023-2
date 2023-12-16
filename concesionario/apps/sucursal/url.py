from django.urls import path
from .forms import SucursalAjaxCreateView, SucursalAjaxUpdateView
from .views import SucursalesListView

urlpatterns = [
    path('sucursal/crear', SucursalAjaxCreateView.as_view(), name='crear'),
    path('sucursal/<int:pk>/', SucursalAjaxUpdateView.as_view(), name='actualizar'),
    path('sucursales/', SucursalesListView.as_view(), name='listar'),
]
