from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import index, login_ren


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="Home"),
    path('iniciologin/', login_ren, name="Iniciologin"),

    path('inicio/', include(('apps.inicio.url', 'inicio'), namespace="inicio")),
    path('cuenta/', include(('apps.cuenta.url', 'cuenta'), namespace='cuenta')),
    path('cotizacion/', include(('apps.cotizacion.url','cotizacion'), namespace='cotizacion')),
    path('cliente/', include(('apps.cliente.url', 'cliente'), namespace="cliente")),
    path('empleado/', include(('apps.empleado.url','empleado'), namespace="empleado")),
    path('repuesto/', include(('apps.repuesto.url', 'repuesto'), namespace="repuesto")),
    path('sucursal/', include(('apps.sucursal.url', 'sucursal'), namespace="sucursal")),
    path('vehiculo/', include(('apps.vehiculo.url','vehiculo'), namespace="vehiculo")),
    path('venta/', include(('apps.venta.url', 'venta'), namespace="venta")),
    path('proveedor/', include(('apps.proveedor.url', 'proveedor'), namespace="proveedor")),
    path('reporte/', include(('apps.reporte.url', 'reporte'), namespace="reporte")),
    path('orden_de_trabajo/', include(('apps.orden_de_trabajo.url', 'orden_de_trabajo'), namespace="orden_de_trabajo")),
    path('cotizacion_orden_de_trabajo/', include(('apps.cotizacion_orden_de_trabajo.url', 'cotizacion_orden_de_trabajo'), namespace="cotizacion_orden_de_trabajo")),
    path('factura_orden_de_trabajo/', include(('apps.factura_orden_de_trabajo.url', 'factura_orden_de_trabajo'), namespace="factura_orden_de_trabajo")),
    path('movil/', include(('apps.movil.url', 'movil'), namespace="movil")),

    # URL for accessing images in the media folder
    # If you're displaying images in your HTML content, this link is necessary to show the images
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add the following line if you want to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
