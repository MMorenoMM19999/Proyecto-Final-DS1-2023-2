# -*- encoding: utf-8 -*-

from django.urls import re_path
from .views import Validar

urlpatterns = [
	
	re_path(r'^validar/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<id>\d+)/', Validar.as_view(), name='validar'),


]
