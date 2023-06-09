# Generated by Django 3.2.12 on 2022-02-18 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('participantes', models.IntegerField(verbose_name='Participantes')),
                ('objetivo', models.CharField(max_length=500, verbose_name='Objetivo')),
                ('descripcion', models.CharField(max_length=2000, verbose_name='Descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividad.categoria')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
    ]
