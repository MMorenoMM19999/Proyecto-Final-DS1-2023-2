# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Count, Sum
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models.functions import Coalesce
from apps.empleado.models import Empleado, VENDEDOR, JEFE_TALLER, GERENTE
from apps.sucursal.models import SucursalVehiculo
from apps.venta.models import Venta
from apps.cotizacion.models import Cotizacion
from apps.sucursal.models import Sucursal

from apps.factura_orden_de_trabajo.models import FacturaOrdenDeTrabajo


class Login(TemplateView):

    # Cuando la petición es tipo POST, se hace el proceso de login con la información del formulario de login
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Usando la función authenticate, obtenemos el usuario que corresponde con los datos
        # pasados como argumentos
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                # Retornamos una respuesta con el perfil del usuario
                return self.get_user_template(request)
            else:
                context = {'message': 'Su usuario no está activo'}
                return render(request, 'inicio/login.html', context)
        else:
            context = {'message': 'Usuario o contraseña inválido'}
            return render(request, 'inicio/login.html', context)

    def get_user_template(self, request):
        try:
            if request.user.empleado.tipo == GERENTE:
                sucursales = Venta.objects.values(
                    'sucursal_vehiculo__sucursal__nombre', 'sucursal_vehiculo__sucursal__ciudad').annotate(total=Sum('precio_venta'))

                num_empleados = Empleado.objects.all().count()

                valor_ventas = Venta.dinero_acumulado(Venta)

                valor_ordenes_de_trabajo = FacturaOrdenDeTrabajo.dinero_en_facturas(
                    FacturaOrdenDeTrabajo)

                vendedores = Empleado.objects.filter(tipo=VENDEDOR).annotate(
                    num_ventas=Count('ventas')).order_by('-num_ventas')

                sucursales_vehiculos = SucursalVehiculo.objects.annotate(
                    num_ventas=Count('ventas')).order_by('-num_ventas')

                context = {
                    'ventas': sucursales,
                    'valor_ordenes_de_trabajo': valor_ordenes_de_trabajo,
                    'valor_ventas': valor_ventas,
                    'num_empleados': num_empleados,
                    'vendedores': vendedores,
                    'sucursales_vehiculos': sucursales_vehiculos
                }

                return render(request, 'cuenta/perfil_gerente.html', context)

            elif request.user.empleado.tipo == VENDEDOR:
                ventasVendedor = Venta.objects.filter(empleado=request.user.empleado).values("empleado").annotate(
                    cantidad=Count('empleado_id')).order_by(Coalesce('cantidad', 'cantidad').desc())
                if ventasVendedor:
                    cantidadVentas = ventasVendedor[0]['cantidad']
                else:
                    cantidadVentas = 0
                    context = {
                        "link": "/admin/venta/venta/add/",
                        "Error": f"Message: Data not provided in Venta"
                    }
                    return render(request, 'cuenta/perfil_jefe_taller.html', context)

                cantidadCotizacion = Cotizacion.objects.filter(empleado=request.user.empleado).values           ("empleado").annotate(cantidadCo=Count('empleado_id')).order_by(Coalesce('cantidadCo', 'cantidadCo').desc())

                if cantidadCotizacion:
                    numeroCotizaciones = cantidadCotizacion[0]['cantidadCo']
                else:
                    numeroCotizaciones = 0
                    context = {
                        "link": "/admin/cotizacion/cotizacion/add/",
                        "Error": f"Message: Data not provided in Cotizacion"
                    }
                    return render(request, 'cuenta/perfil_jefe_taller.html', context)


                sucursalEmpleado = request.user.empleado.sucursal

                cantidadVehiculos = SucursalVehiculo.objects.filter(sucursal=sucursalEmpleado).values("sucursal").annotate(
                    cantidad=Sum('cantidad')).order_by(Coalesce('cantidad', 'cantidad').desc())
                numeroVehiculos = cantidadVehiculos[0]['cantidad']

                if cantidadVehiculos:
                    numeroVehiculos = cantidadVehiculos[0]['cantidad']
                else:
                    numeroVehiculos = 0
                    context = {
                        "link": "/admin/sucursal/sucursalvehiculo/add/",
                        "Error": f"Message: Data not provided in sucursal vehiculo"
                    }
                    return render(request, 'cuenta/perfil_jefe_taller.html', context)

                cotizacionesEmpleado = Cotizacion.objects.filter(
                    empleado=request.user.empleado)

                if cotizacionesEmpleado:
                    pass
                else:
                    cotizacionesEmpleado = "0"
                    context = {

                        'cantidadVentas': cantidadVentas,
                        'numeroCotizaciones': numeroCotizaciones,
                        'numeroVehiculos': numeroVehiculos,
                        'cotizacionesEmpleado': cotizacionesEmpleado

                    }
                    return render(request, 'cuenta/perfil_vendedor.html', context)

                context = {
                    'cantidadVentas': cantidadVentas,
                    'numeroCotizaciones': numeroCotizaciones,
                    'numeroVehiculos': numeroVehiculos,
                    'cotizacionesEmpleado': cotizacionesEmpleado
                }

                return render(request, 'cuenta/perfil_vendedor.html', context)

            elif request.user.empleado.tipo == JEFE_TALLER:
                return render(request, 'cuenta/perfil_jefe_taller.html')
        except AttributeError as e:
            context = {
                "Error": f"Message: {e}",
                "link": "/admin/empleado/empleado/add/"
            }
            return render(request, 'cuenta/perfil_jefe_taller.html', context)


class Logout(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        context = {}
        return render(request, 'inicio/login.html', context)


class RecuperarLogin(PasswordResetView):
    template_name = 'inicio/recuperar_login_form.html'
    email_template_name = 'inicio/recuperar_login_email.html'
    subject_template_name = 'inicio/recuperar_login_email_asunto.txt'
    success_url = reverse_lazy('inicio:recuperar_login_email_enviado')


class RecuperarLoginEmailEnviado(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        return render(request, 'inicio/recuperar_login_email_enviado.html')


class RecuperarLoginConfirmacion(PasswordResetConfirmView):
    template_name = 'inicio/recuperar_login_confirmacion.html'
    success_url = reverse_lazy('inicio:recuperar_login_terminado')


class RecuperarLoginTerminado(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        return render(request, 'inicio/recuperar_login_terminado.html',)
