# Generated by Django 2.1.7 on 2019-02-22 14:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_ingreso', models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 50, 10, 686045))),
                ('historia', models.TextField(max_length=100)),
                ('proxima_tarea', models.CharField(choices=[('Llamar', 'Llamar'), ('Re-Cotizar', 'Re-Cotizar'), ('Correo', 'Correo'), ('Visita', 'Visita')], max_length=30)),
                ('estado', models.CharField(choices=[('Vendida', 'Vendida'), ('Pendiente', 'Pendiente'), ('Desierta', 'Desierta')], max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 50, 10, 676045)),
        ),
        migrations.AddField(
            model_name='historia_cotizacion',
            name='id_historia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizaciones.Cotizacion'),
        ),
        migrations.AddField(
            model_name='historia_cotizacion',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]