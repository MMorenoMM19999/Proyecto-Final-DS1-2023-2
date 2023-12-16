# -*- encoding: utf-8 -*-

# Corrected import statement
from django.urls import include, re_path

# Your other import statements...

from .views import ProveedorListView
from .forms import ProveedorCreateView, ProveedorUpdateView

# Updated URL patterns
# Updated URL patterns
urlpatterns = [
    re_path(r'^proveedor/crear/$', ProveedorCreateView.as_view(), name='crear'),
    re_path(r'^proveedor/(?P<pk>\d+)/$', ProveedorUpdateView.as_view(), name='actualizar'),
    re_path(r'^proveedores/$', ProveedorListView.as_view(), name='listar'),
]
