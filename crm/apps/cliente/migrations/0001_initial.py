# Generated by Django 2.1.7 on 2019-02-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dependencia', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Giro_Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_giro', models.CharField(max_length=20)),
                ('descripcion_giro', models.TextField(max_length=70)),
            ],
        ),
    ]
