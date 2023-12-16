# -*- encoding: utf-8 -*-
from django.urls import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from .models import Cotizacion
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
from django.contrib import messages


class CrearCotizacion(CreateView):
    fecha_vencimiento = forms.DateField(
        widget=forms.widgets.DateInput(format="%y-%m-%d"))
    model = Cotizacion
    fields = ['cliente', 'vehiculo', 'fecha_vencimiento', 'forma_pago']

    def get_context_data(self, **kwargs):

        context = super(CrearCotizacion, self).get_context_data(**kwargs)
        context['search_button_text'] = 'Completar Formulario'

        clientes = Cliente.objects.all()
        context['lista_clientes'] = clientes

        vehiculos = Vehiculo.objects.all()
        context['vehiculos'] = vehiculos

        return context

    def post(self, request, *args, **kwargs):

        empleado = Empleado.objects.get(user_id=self.request.user.id)
        cliente = Cliente.objects.get(pk=request.POST.get("cliente"))
        vehiculo = Vehiculo.objects.get(pk=request.POST.get("vehiculo"))
        forma_pago = request.POST.get("forma_pago")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")
        # print fecha_vencimiento
        cotizacion = Cotizacion(empleado=empleado, cliente=cliente, vehiculo=vehiculo,
                                fecha_vencimiento=fecha_vencimiento, forma_pago=forma_pago)
        cotizacion.save()
        context = {'cotizacion': cotizacion}
        return render(request,'cotizacion/cotizacionPDF.html',context)


class ActualizarCotizacion(UpdateView):
    model = Cotizacion
    fields = ['empleado', 'cliente', 'vehiculo',
              'fecha', 'fecha_vencimiento', 'forma_pago']

    def get_success_url(self):
        messages.info(self.request, "Cotización creada con éxito")
        return reverse_lazy('cotizacion:listar')
