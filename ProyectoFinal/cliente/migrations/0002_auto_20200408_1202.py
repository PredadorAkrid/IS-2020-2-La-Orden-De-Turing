# Generated by Django 3.0.3 on 2020-04-08 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name_plural': 'Direcciones'},
        ),
    ]
