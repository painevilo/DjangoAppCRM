# Generated by Django 2.1.7 on 2019-02-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=20)),
                ('nombre_producto', models.CharField(max_length=20)),
                ('descripcion_producto', models.TextField(max_length=70)),
                ('precio_producto', models.IntegerField()),
            ],
        ),
    ]
