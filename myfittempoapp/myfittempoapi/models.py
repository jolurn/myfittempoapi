from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# from myfittempoapi.lib.db import ds

Es1 = 'A'
Es2 = 'I'
ESTADO_OFERTA = [
    (Es1, 'Activo'),
  (Es2, 'Inactivo')
  ]

class User(AbstractUser):
  email =models.EmailField(unique=True)
  primerNombre = models.CharField(max_length=50)
  segundoNombre = models.CharField(max_length=50, null=True, blank=True)
  apellidoPaterno = models.CharField(max_length=100)
  apellidoMaterno = models.CharField(max_length=100)
  dni = models.IntegerField(null=True)
  celular = models.IntegerField(null=True)  
  direccion = models.CharField(max_length=100)
  usuario_activo = models.BooleanField(default=True)  
  usu_tipo = models.CharField(max_length=45,null=True, blank=True)
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)

  REQUIRED_FIELDS = ['email','primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','direccion']

  def nombre_completo(self):
    return "{} {}, {} {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre, self.segundoNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Usuarios"

class Cliente(models.Model):
  
  usuarios = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  fechaNacimiento = models.DateField()
  distrito = models.CharField(max_length=100,null=True, blank=True)
  fotoCliente = models.ImageField(null=True, upload_to='img')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  

  def nombre_completo(self):
    return "{} {}, {} {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre , self.segundoNombre)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Clientes"

class Empleado(models.Model):
  
  usuarios = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
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
  
  
  def nombre_completo(self):
    return "{} {}, {} {}".format(self.usuarios.apellidoPaterno, self.usuarios.apellidoMaterno, self.usuarios.primerNombre, self.usuarios.segundoNombre)
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
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)
  

  def nombre_completo(self):
    return "{} {}, {}".format(self.empleado.usuarios.apellidoPaterno, self.empleado.usuarios.apellidoMaterno, self.horaInicio)
  def __str__(self):
        return self.nombre_completo()
  class Meta:
        verbose_name_plural = "Ofertas"

class Carrito(models.Model):
  
  cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
  estadoCarrito = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='I')
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  ofertas = models.ManyToManyField(Oferta, through='CarritoOferta')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)

  class Meta:
        verbose_name_plural = "Carritos"

class CarritoOferta(models.Model):
  
  carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
  oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
  fechaRegistro = models.DateField(default=datetime.now())
  fechaModificado = models.DateField(null=True, blank=True)
  fechaElimnado = models.DateField(null=True, blank=True)