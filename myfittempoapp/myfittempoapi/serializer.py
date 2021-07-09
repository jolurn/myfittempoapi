# from typing_extensions import Required
from rest_framework import serializers
from myfittempoapi.models import Cliente,Empleado,Oferta,Carrito
from datetime import datetime


class ClienteSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  correo = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)


  def create(self, validated_data):
    cliente = Cliente()
        
    cliente.primerNombre = validated_data['primerNombre']
    cliente.segundoNombre = validated_data['segundoNombre']
    cliente.apellidoPaterno = validated_data['apellidoPaterno']
    cliente.apellidoMaterno = validated_data['apellidoMaterno']
    cliente.dni = validated_data['dni']
    cliente.celular = validated_data['celular']
    cliente.correo = validated_data['correo']
    cliente.password = validated_data['password']
    cliente.direccion = validated_data['direccion']

    cliente.save()
    return cliente

class ClienteUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  correo = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)

  def update(self, queryset, validated_data):
    
    cliente = queryset
    cliente.primerNombre = validated_data['primerNombre']
    cliente.segundoNombre = validated_data['segundoNombre']
    cliente.apellidoPaterno = validated_data['apellidoPaterno']
    cliente.apellidoMaterno = validated_data['apellidoMaterno']
    cliente.dni = validated_data['dni']
    cliente.celular = validated_data['celular']
    cliente.correo = validated_data['correo']
    cliente.password = validated_data['password']
    cliente.direccion = validated_data['direccion']
    cliente.fechaModificado = datetime.now()

    cliente.save()
    return cliente

class EmpleadoSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  correo = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  distrito = serializers.CharField(max_length=100)
  profesion = serializers.CharField(max_length=50)
  descripcion = serializers.CharField(max_length=200)
  fotoPerfil = serializers.ImageField()
  fotoBanner = serializers.ImageField()
  video = serializers.FileField()
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)

  def create(self,validated_data):
    empleado = Empleado()

    empleado.primerNombre = validated_data['primerNombre']
    empleado.segundoNombre = validated_data['segundoNombre']
    empleado.apellidoPaterno = validated_data['apellidoPaterno']
    empleado.apellidoMaterno = validated_data['apellidoMaterno']
    empleado.dni = validated_data['dni']
    empleado.celular = validated_data['celular']
    empleado.correo = validated_data['correo']
    empleado.password = validated_data['password']
    empleado.direccion = validated_data['direccion']
    empleado.distrito = validated_data['distrito']
    empleado.profesion = validated_data['profesion']
    empleado.descripcion = validated_data['descripcion']
    empleado.fotoPerfil = validated_data['fotoPerfil']
    empleado.fotoBanner = validated_data['fotoBanner']
    empleado.video = validated_data['video']
    
    empleado.save()
    return empleado

class EmpleadoUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  correo = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  distrito = serializers.CharField(max_length=100)
  profesion = serializers.CharField(max_length=50)
  descripcion = serializers.CharField(max_length=200)
  fotoPerfil = serializers.ImageField()
  fotoBanner = serializers.ImageField()
  video = serializers.FileField()
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)

  def update(self, queryset, validated_data):

    empleado = queryset
    empleado.primerNombre = validated_data['primerNombre']
    empleado.segundoNombre = validated_data['segundoNombre']
    empleado.apellidoPaterno = validated_data['apellidoPaterno']
    empleado.apellidoMaterno = validated_data['apellidoMaterno']
    empleado.dni = validated_data['dni']
    empleado.celular = validated_data['celular']
    empleado.correo = validated_data['correo']
    empleado.password = validated_data['password']
    empleado.direccion = validated_data['direccion']
    empleado.distrito = validated_data['distrito']
    empleado.profesion = validated_data['profesion']
    empleado.descripcion = validated_data['descripcion']
    empleado.fotoPerfil = validated_data['fotoPerfil']
    empleado.fotoBanner = validated_data['fotoBanner']
    empleado.video = validated_data['video']
    empleado.fechaModificado = datetime.now()

    empleado.save()
    return empleado
    
class OfertaSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  empleado = EmpleadoSerializer()
  fechaOferta = serializers.DateField()
  horaInicio = serializers.TimeField()
  horaFin = serializers.TimeField()
  costo = serializers.FloatField()
  estadoOferta = serializers.CharField(max_length=1)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)
  init_point = serializers.CharField(max_length=250)

  def create(self,validated_data):
    oferta = Oferta()

    oferta.empleado = validated_data['empleado']
    oferta.fechaOferta = validated_data['fechaOferta']
    oferta.horaInicio = validated_data['horaInicio']
    oferta.horaFin = validated_data['horaFin']
    oferta.costo = validated_data['costo']
    oferta.estadoOferta = validated_data['estadoOferta']

    oferta.save()
    return oferta

class OfertaUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  empleado = EmpleadoSerializer()
  fechaOferta = serializers.DateField()
  horaInicio = serializers.TimeField()
  horaFin = serializers.TimeField()
  costo = serializers.FloatField()
  estadoOferta = serializers.CharField(max_length=1)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)
  
  def update(self, queryset, validated_data):

    oferta = queryset
    oferta.empleado = validated_data['empleado']
    oferta.fechaOferta = validated_data['fechaOferta']
    oferta.horaInicio = validated_data['horaInicio']
    oferta.horaFin = validated_data['horaFin']
    oferta.costo = validated_data['costo']
    oferta.estadoOferta = validated_data['estadoOferta']
    oferta.fechaModificado = datetime.now()

    oferta.save()
    return oferta

class CarritoSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  cliente = ClienteSerializer()
  estadoCarrito = serializers.CharField(max_length=1)
  estado = serializers.CharField(max_length=1)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)
  ofertas = OfertaSerializer(many=True)
 
class CarritoSaveSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  cliente = serializers.ReadOnlyField(source='Cliente')
  estadoCarrito = serializers.CharField(max_length=1)
  estado = serializers.CharField(max_length=1)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)
  ofertas = serializers.ListField()

  def create(self,validated_data):
    carrito = Carrito()
    
    carrito.estadoCarrito = validated_data['estadoCarrito']
    carrito.estado = validated_data['estado']
    
    for item in validated_data['cliente']:
      cliente = Cliente.objects.filter(pk=item.id).last()
      if cliente == None:
        cliente = Cliente()
        cliente.id=item.id
        cliente.save()
      Carrito.cliente.add(cliente)

    for item in validated_data['ofertas']:
      oferta = Oferta.objects.filter(pk=item.id).last()
      if oferta == None:
        oferta = Oferta()
        oferta.id=item.id
        oferta.save()      
      carrito.ofertas.add(oferta)
    
    carrito.save()
    return carrito