# Generated by Django 5.0 on 2023-12-13 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repuesto', '0001_initial'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='SucursalRepuesto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('repuesto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='repuesto.repuesto')),
                ('sucursal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
            ],
            options={
                'verbose_name_plural': 'Repuestos Sucursal',
                'ordering': ['cantidad'],
                'unique_together': {('sucursal', 'repuesto')},
            },
        ),
        migrations.AddField(
            model_name='sucursal',
            name='repuestos',
            field=models.ManyToManyField(default='', related_name='sucursal', through='sucursal.SucursalRepuesto', to='repuesto.repuesto'),
        ),
        migrations.CreateModel(
            name='SucursalVehiculo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('sucursal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
                ('vehiculo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.vehiculo')),
            ],
            options={
                'verbose_name_plural': 'Vehiculos Sucursal',
                'ordering': ['cantidad'],
                'unique_together': {('sucursal', 'vehiculo', 'color')},
            },
        ),
        migrations.AddField(
            model_name='sucursal',
            name='vehiculos',
            field=models.ManyToManyField(default='', related_name='sucursal', through='sucursal.SucursalVehiculo', to='vehiculo.vehiculo'),
        ),
        migrations.AlterUniqueTogether(
            name='sucursal',
            unique_together={('nombre', 'ciudad')},
        ),
    ]
