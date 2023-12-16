# -*- encoding: utf-8 -*-

from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(null=True, blank=True, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=100)
    apellido = models.CharField(null=True, blank=True, max_length=100)
    ciudad = models.CharField(null=True, blank=True, max_length=100)
    departamento = models.CharField(null=True, blank=True, max_length=100)
    telefono = models.CharField(null=True, blank=True, max_length=100)
    celular = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(null=True, blank=True, max_length=100)
    habilitado = models.BooleanField(default=True)

    # Explicitly defining BigAutoField as the primary key
    id = models.BigAutoField(primary_key=True)

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre + " " + self.apellido
