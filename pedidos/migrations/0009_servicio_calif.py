# Generated by Django 4.0 on 2021-12-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_servicio_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='calif',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
