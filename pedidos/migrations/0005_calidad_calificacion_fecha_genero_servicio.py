# Generated by Django 4.0 on 2021-12-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_rename_user_profile_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='calidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calidad', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'calidad',
                'verbose_name_plural': 'calidades',
            },
        ),
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.CharField(max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'calificacion',
                'verbose_name_plural': 'calificaciones',
            },
        ),
        migrations.CreateModel(
            name='fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'fecha',
                'verbose_name_plural': 'fechas',
            },
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'genero',
                'verbose_name_plural': 'generos',
            },
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo1', models.CharField(max_length=50, unique=True)),
                ('titulo2', models.CharField(blank=True, max_length=50, null=True)),
                ('titulo3', models.CharField(blank=True, max_length=50, null=True)),
                ('titulo4', models.CharField(blank=True, max_length=50, null=True)),
                ('tlim1', models.CharField(blank=True, max_length=50, null=True)),
                ('tlim2', models.CharField(blank=True, max_length=50, null=True)),
                ('tlim3', models.CharField(blank=True, max_length=50, null=True)),
                ('tlim4', models.CharField(blank=True, max_length=50, null=True)),
                ('sinop', models.CharField(blank=True, max_length=200, null=True)),
                ('peso', models.FloatField()),
                ('imagen', models.ImageField(upload_to='servicios')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('calidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pedidos.calidad')),
                ('calificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pedidos.calificacion')),
                ('fecha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pedidos.fecha')),
                ('genero', models.ManyToManyField(to='pedidos.genero')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]
