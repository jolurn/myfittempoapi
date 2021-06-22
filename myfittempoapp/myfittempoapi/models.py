from django.db import models
from datetime import date

Es1 = 'A'
Es2 = 'I'
ESTADO_OFERTA = [
    (Es1, 'Activo'),
  (Es2, 'Inactivo')
  ]
# Create your models here.
class Cliente(models.Model):

  # idCliente = models.AutoField(primary_key=True)
  primerNombre = models.CharField(max_length=50)
  segundoNombre = models.CharField(max_length=50, null=True, blank=True)
  apellidoPaterno = models.CharField(max_length=100)
  apellidoMaterno = models.CharField(max_length=100)
  dni = models.IntegerField()
  celular = models.IntegerField()
  correo = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  fechaRegistro = date.today()
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)

  def nombre_completo(self):
    return "{} {}, {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Clientes"

class Empleado(models.Model):

  # idEmpleado = models.AutoField(primary_key=True)
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
  profesión = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=200)
  fotoPerfil = models.CharField(max_length=100, null=True, blank=True)
  fotoBanner = models.CharField(max_length=100, null=True, blank=True)
  video = models.CharField(max_length=100, null=True, blank=True)
  fechaRegistro = date.today()
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  
  def nombre_completo(self):
    return "{} {}, {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Empleados"

class Oferta(models.Model):
  
  # idOferta = models.AutoField(primary_key=True)
  empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
  fechaOferta = models.DateField()
  horaInicio = models.TimeField()
  horaFin = models.TimeField()
  costo = models.FloatField()
  estadoOferta = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = date.today()
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)

  def nombre_completo(self):
    return "{} {}, {}".format(self.empleado.apellidoMaterno, self.empleado.apellidoPaterno, self.horaInicio)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Ofertas"

class Carrito(models.Model):
  idCarrito = models.AutoField(primary_key=True)
  # cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
  estadoCarrito = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = date.today()
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  ofertas = models.ManyToManyField(Oferta)

  class Meta:
        verbose_name_plural = "Carritos"