# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Venta 
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView


class ListaVentas(ListView): 
	model = Venta
	context_object_name = 'lista_ventas'


class FacturaCreateView(TemplateView):
	def get(self,request,*args,**kwargs):
		venta= Venta.objects.get(id=kwargs['pk'])
		context = {'venta':venta}

		return render(request,'venta/factura.html',context)