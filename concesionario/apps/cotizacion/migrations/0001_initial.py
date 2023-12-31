# Generated by Django 5.0 on 2023-12-13 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('empleado', '0001_initial'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('forma_pago', models.CharField(choices=[('Credito', 'Credito'), ('Efectivo', 'Efectivo'), ('Tarjeta_credito', 'Tarjeta de credito'), ('Tarjeta_debito', 'Tarjeta de debito')], default='Efectivo', max_length=20)),
                ('habilitado', models.BooleanField(default=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('empleado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
                ('vehiculo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.vehiculo')),
            ],
            options={
                'verbose_name_plural': 'Cotizaciones',
                'ordering': ['fecha'],
            },
        ),
    ]
