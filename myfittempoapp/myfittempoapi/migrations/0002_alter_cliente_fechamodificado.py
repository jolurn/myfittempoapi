# Generated by Django 3.2.4 on 2021-06-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfittempoapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fechaModificado',
            field=models.DateField(null=True),
        ),
    ]
