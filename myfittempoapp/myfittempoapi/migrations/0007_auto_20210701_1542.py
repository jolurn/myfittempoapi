# Generated by Django 3.2.4 on 2021-07-01 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfittempoapi', '0006_auto_20210626_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='empleado',
            name='estado',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 15, 42, 16, 699659)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaModificado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 15, 42, 16, 695631)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 15, 42, 16, 697129)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 15, 42, 16, 698629)),
        ),
    ]