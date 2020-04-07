# Generated by Django 3.0.3 on 2020-04-07 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(db_column='id_cliente', primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=64)),
                ('apellido_pa_cliente', models.CharField(max_length=100)),
                ('apellido_ma_cliente', models.CharField(max_length=100)),
                ('telefono_cliente', models.CharField(max_length=10)),
                ('user_cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_direccion', models.CharField(max_length=200)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Cliente')),
            ],
            options={
                'db_table': 'direccion',
                'unique_together': {('id_cliente', 'descripcion_direccion')},
            },
        ),
    ]
