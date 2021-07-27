# Generated by Django 3.2.5 on 2021-07-26 15:13

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('primerNombre', models.CharField(max_length=50)),
                ('segundoNombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidoPaterno', models.CharField(max_length=100)),
                ('apellidoMaterno', models.CharField(max_length=100)),
                ('dni', models.IntegerField(null=True)),
                ('celular', models.IntegerField(null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usu_tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 150255))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoCarrito', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='I', max_length=1)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 154257))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('fechaElimnado', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Carritos',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fotoPerfil', models.ImageField(null=True, upload_to='img')),
                ('fotoBanner', models.ImageField(null=True, upload_to='img')),
                ('video', models.FileField(null=True, upload_to='video')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 153256))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('fechaElimnado', models.DateField(blank=True, null=True)),
                ('usuarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaOferta', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('costo', models.FloatField()),
                ('estadoOferta', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 153756))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('fechaElimnado', models.DateField(blank=True, null=True)),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfittempoapi.empleado')),
            ],
            options={
                'verbose_name_plural': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaNacimiento', models.DateField()),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('fotoCliente', models.ImageField(null=True, upload_to='img')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 152256))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('fechaElimnado', models.DateField(blank=True, null=True)),
                ('usuarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='CarritoOferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2021, 7, 26, 10, 13, 37, 155258))),
                ('fechaModificado', models.DateField(blank=True, null=True)),
                ('fechaElimnado', models.DateField(blank=True, null=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfittempoapi.carrito')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfittempoapi.oferta')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfittempoapi.cliente'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='ofertas',
            field=models.ManyToManyField(through='myfittempoapi.CarritoOferta', to='myfittempoapi.Oferta'),
        ),
    ]
