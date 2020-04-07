# Generated by Django 3.0.3 on 2020-04-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id_repatidor', models.AutoField(db_column='id_repatidor', primary_key=True, serialize=False)),
                ('nombre_repartidor', models.CharField(max_length=64)),
                ('apellido_paterno_repartidor', models.CharField(max_length=100)),
                ('apellido_materno_repartidor', models.CharField(max_length=100)),
                ('correo_repartidor', models.EmailField(max_length=254)),
                ('password_repartidor', models.CharField(max_length=16)),
            ],
        ),
    ]
