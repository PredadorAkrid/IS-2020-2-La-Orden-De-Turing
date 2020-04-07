# Generated by Django 3.0.3 on 2020-04-07 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('platillo', '0001_initial'),
        ('cliente', '0001_initial'),
        ('repartidor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('precio_orden', models.IntegerField(default=0)),
                ('direccion_entrega', models.CharField(max_length=200)),
                ('id_cliente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='cliente.Cliente')),
                ('id_platillo', models.ManyToManyField(null=True, to='platillo.Platillo')),
                ('id_repartidor', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='repartidor.Repartidor')),
            ],
        ),
    ]
