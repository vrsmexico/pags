# Generated by Django 4.0 on 2021-12-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0012_pedidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='content',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
