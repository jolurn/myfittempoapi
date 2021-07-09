# Generated by Django 3.2.4 on 2021-07-02 20:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myfittempoapi', '0008_auto_20210701_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 2, 15, 42, 9, 801426)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 2, 15, 42, 9, 799425)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 2, 15, 42, 9, 800425)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 7, 2, 15, 42, 9, 800926)),
        ),
    ]