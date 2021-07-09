from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from myfittempoapi.lib.db import ds

Es1 = 'A'
Es2 = 'I'
ESTADO_OFERTA = [
    (Es1, 'Activo'),
  (Es2, 'Inactivo')
  ]
# Create your models here.



class Cliente(models.Model):
  
  primerNombre = models.CharField(max_length=50)
  segundoNombre = models.CharField(max_length=50, null=True, blank=True)
  apellidoPaterno = models.CharField(max_length=100)
  apellidoMaterno = models.CharField(max_length=100)
  dni = models.IntegerField()
  celular = models.IntegerField()
  correo = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  

  def nombre_completo(self):
    return "{} {}, {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Clientes"

class Empleado(models.Model):

  primerNombre = models.CharField(max_length=50)
  segundoNombre = models.CharField(max_length=50, null=True, blank=True)
  apellidoPaterno = models.CharField(max_length=100)
  apellidoMaterno = models.CharField(max_length=100)
  dni = models.IntegerField()
  celular = models.IntegerField()
  correo = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  distrito = models.CharField(max_length=100)
  profesion = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=200)
  fotoPerfil = models.ImageField(null=True, upload_to='img')
  fotoBanner = models.ImageField(null=True, upload_to='img')
  video = models.FileField(null=True, upload_to='video')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  
  # print(fotoPerfil)

  def nombre_completo(self):
    return "{} {}, {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Empleados"

class Oferta(models.Model):
  
  empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
  fechaOferta = models.DateField()
  horaInicio = models.TimeField()
  horaFin = models.TimeField()
  costo = models.FloatField()
  estadoOferta = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  init_point = models.CharField(max_length=250, null=True)

  def nombre_completo(self):
    return "{} {}, {}".format(self.empleado.apellidoMaterno, self.empleado.apellidoPaterno, self.horaInicio)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Ofertas"

class Carrito(models.Model):
  
  cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
  estadoCarrito = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  ofertas = models.ManyToManyField(Oferta)

  class Meta:
        verbose_name_plural = "Carritos"