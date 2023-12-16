# -*- encoding: utf-8 -*-

from django.urls import include, path, re_path
from django.contrib import admin
from .views import Login, Logout
from .views import RecuperarLogin
from .views import RecuperarLoginEmailEnviado
from .views import RecuperarLoginConfirmacion
from .views import RecuperarLoginTerminado

urlpatterns = [
    # For the inicio and cierre de sesion
 
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    # For the recuperacion de la cuenta
    # Sends to the form to confirm the email of the person who forgot their login
    path('recuperar_login/', RecuperarLogin.as_view(), name='recuperar_login'),
    # Shows a notice that indicates that a message has been sent to the email
    # This message will have a temporary link that will allow showing a password recovery form
    path('recuperar_login_email_enviado/', RecuperarLoginEmailEnviado.as_view(), name='recuperar_login_email_enviado'),
    # Processes the generated URL to recover the user's login
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', RecuperarLoginConfirmacion.as_view(), name='recuperar_login_confirmacion'),
    # Shows a message confirming that the login recovery process has been completed
    path('recuperar_login_terminado', RecuperarLoginTerminado.as_view(), name='recuperar_login_terminado'),
]
