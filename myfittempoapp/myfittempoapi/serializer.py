# from typing_extensions import Required
from rest_framework import serializers
from myfittempoapi.models import Cliente
import datetime
# from datetime import date

Es1 = 'A'
Es2 = 'I'
ESTADO_OFERTA = [(Es1, 'Activo'),(Es2, 'Inactivo')]

class ClienteSerializer(serializers.Serializer):
  class Meta:    
    validators = []

  # id = serializers.IntegerField()
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  correo = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  fechaRegistro = serializers.DateField(required=False, default=datetime.date.today)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)


  def create(self, validated_data):
    cliente = Cliente()
    
    # cliente.idCliente = validated_data['idCliente']
    cliente.primerNombre = validated_data['primerNombre']
    cliente.segundoNombre = validated_data['segundoNombre']
    cliente.apellidoPaterno = validated_data['apellidoPaterno']
    cliente.apellidoMaterno = validated_data['apellidoMaterno']
    cliente.dni = validated_data['dni']
    cliente.celular = validated_data['celular']
    cliente.correo = validated_data['correo']
    cliente.password = validated_data['password']
    cliente.direccion = validated_data['direccion']
    cliente.fechaRegistro = validated_data['fechaRegistro']
    # cliente.fechaModificado = validated_data['fechaModificado']
    # cliente.fechaElimnado = validated_data['fechaElimnado']
    cliente.save()

    return cliente
# class EmpleadoSerializer(serializers.Serializer):
#   idEmpleado = serializers.AutoField(primary_key=True)
#   primerNombre = serializers.CharField(max_length=50, null=True, blank=True)
#   segundoNombre = serializers.CharField(max_length=50)
#   apellidoPaterno = serializers.CharField(max_length=100)
#   apellidoMaterno = serializers.CharField(max_length=100)
#   dni = serializers.IntegerField()
#   celular = serializers.IntegerField()
#   correo = serializers.CharField(max_length=100)
#   password = serializers.CharField(max_length=100)
#   direccion = serializers.CharField(max_length=100)
#   distrito = serializers.CharField(max_length=100)
#   profesión = serializers.CharField(max_length=50)
#   descripcion = serializers.CharField(max_length=200)
#   fotoPerfil = serializers.CharField(max_length=100, null=True, blank=True)
#   fotoBanner = serializers.CharField(max_length=100, null=True, blank=True)
#   video = serializers.CharField(max_length=100, null=True, blank=True)
#   fechaRegistro = serializers.date.today()
#   fechaModificado = serializers.DateField(null=True, blank=True)
#   fechaElimnado = serializers.DateField(null=True, blank=True)

# class OfertaSerializer(serializers.Serializer):
#   idOferta = serializers.AutoField(primary_key=True)
#   empleado = serializers.ForeignKey(EmpleadoSerializer, null=True, blank=True, on_delete=serializers.CASCADE)
#   fechaOferta = serializers.DateField()
#   horaInicio = serializers.TimeField()
#   horaFin = serializers.TimeField()
#   costo = serializers.FloatField()
#   estadoOferta = serializers.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
#   fechaRegistro = serializers.date.today()
#   fechaModificado = serializers.DateField(null=True, blank=True)
#   fechaElimnado = serializers.DateField(null=True, blank=True)

# class CarritoSerializer(serializers.Serializer):
#   idCarrito = serializers.AutoField(primary_key=True)
#   cliente = serializers.ForeignKey(ClienteSerializer, null=True, blank=True, on_delete=serializers.CASCADE)
#   estadoCarrito = serializers.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
#   estado = serializers.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
#   fechaRegistro = serializers.date.today()
#   fechaModificado = serializers.DateField(null=True, blank=True)
#   fechaElimnado = serializers.DateField(null=True, blank=True)
#   ofertas = OfertaSerializer(many=True)