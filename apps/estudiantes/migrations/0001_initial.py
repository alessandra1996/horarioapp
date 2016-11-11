# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-11 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_alumno', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=60)),
                ('id_alumno', models.CharField(max_length=11)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asig_jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_asignaturas', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
                ('creditos', models.IntegerField()),
                ('numero_horas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_dias', models.IntegerField()),
                ('dia', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ['codigo_dias'],
            },
        ),
        migrations.CreateModel(
            name='Franja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_franja', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FranjaDiasHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_dias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Dias')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_hora', models.IntegerField()),
                ('hora', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idhorario', models.IntegerField()),
                ('codigo_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Alumno')),
                ('codigo_jornada', models.ManyToManyField(to='estudiantes.Asig_jornada')),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_jornada', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_academico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pa', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_tipo', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='codigo_pa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Periodo_academico'),
        ),
        migrations.AddField(
            model_name='franjadiashora',
            name='codigo_hora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Hora'),
        ),
        migrations.AddField(
            model_name='franjadiashora',
            name='franja',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Franja'),
        ),
        migrations.AddField(
            model_name='asignaturas',
            name='codigo_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Tipo'),
        ),
        migrations.AddField(
            model_name='asig_jornada',
            name='codigo_asignaturas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Asignaturas'),
        ),
        migrations.AddField(
            model_name='asig_jornada',
            name='codigo_franja',
            field=models.ManyToManyField(to='estudiantes.Franja'),
        ),
        migrations.AddField(
            model_name='asig_jornada',
            name='codigo_jornada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Jornada'),
        ),
    ]
