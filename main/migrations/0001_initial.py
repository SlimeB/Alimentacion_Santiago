# Generated by Django 4.0.2 on 2022-06-07 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria_usuario',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre_categoria', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_restaurante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('contraseña_usuario', models.CharField(max_length=20)),
                ('categoria_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoria_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_producto', models.CharField(max_length=500)),
                ('disponible', models.BooleanField(default=False)),
                ('restaurante_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.restaurante')),
            ],
        ),
    ]
