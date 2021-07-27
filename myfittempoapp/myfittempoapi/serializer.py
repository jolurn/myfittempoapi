# from typing_extensions import Required
from myfittempoapi.models import CarritoOferta
from rest_framework import serializers
from myfittempoapi.models import Cliente,Empleado,Oferta,Carrito,User
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


servidor = "http://d65285feadd4.ngrok.io"
updatefile = "http://d65285feadd4.ngrok"

class CustomObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["primerNombre"] = user.primerNombre
        token["segundoNombre"] = user.segundoNombre
        token["apellidoPaterno"] = user.apellidoPaterno
        token["apellidoMaterno"] = user.apellidoMaterno
        token["usu_tipo"] = user.usu_tipo
        return token

class UserSerializer(serializers.Serializer):

  # id = serializers.IntegerField() No activar por que no va dejar crear usuarios en la parte de admin OjO
  username = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=300)
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  email = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  usu_tipo = serializers.CharField(max_length=50)

  def create(self, validated_data):
    usuario = User()
        
    usuario.username = validated_data['username']
    usuario.set_password(validated_data['password'])
    usuario.primerNombre = validated_data['primerNombre']
    usuario.segundoNombre = validated_data['segundoNombre']
    usuario.apellidoPaterno = validated_data['apellidoPaterno']
    usuario.apellidoMaterno = validated_data['apellidoMaterno']
    usuario.dni = validated_data['dni']
    usuario.celular = validated_data['celular']
    usuario.email = validated_data['email']
    usuario.direccion = validated_data['direccion']
    usuario.usu_tipo = validated_data['usu_tipo']

    usuario.save()
    return usuario

class UsuarioDeleteSerializer(serializers.Serializer):
  
  def delete(self,queryset,validated_data):
    usuario = queryset

    usuario.usuario_activo = 0
    usuario.fechaElimnado = datetime.now()
    
    usuario.save()
    return usuario

class UsuarioUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  username = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=300)
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  email = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  usu_tipo = serializers.CharField(max_length=50)
  
  def update(self,queryset,validated_data):
    usuario = queryset
    
    usuario.username = validated_data['username']
    usuario.set_password(validated_data['password'])
    usuario.primerNombre = validated_data['primerNombre']
    usuario.segundoNombre = validated_data['segundoNombre']
    usuario.apellidoPaterno = validated_data['apellidoPaterno']
    usuario.apellidoMaterno = validated_data['apellidoMaterno']
    usuario.dni = validated_data['dni']
    usuario.celular = validated_data['celular']
    usuario.email = validated_data['email']
    usuario.direccion = validated_data['direccion']
    usuario.usu_tipo = validated_data['usu_tipo'] 
    usuario.fechaModificado = datetime.now()
        
    usuario.save()
    return usuario

class UserClienteSerializer(serializers.Serializer):

  # no agregar id por que se esta usando
  username = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=300)
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  email = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  #no agregar el usu_tipo

  def create(self, validated_data):
    usuario = User()
        
    usuario.username = validated_data['username']
    usuario.set_password(validated_data['password'])
    usuario.primerNombre = validated_data['primerNombre']
    usuario.segundoNombre = validated_data['segundoNombre']
    usuario.apellidoPaterno = validated_data['apellidoPaterno']
    usuario.apellidoMaterno = validated_data['apellidoMaterno']
    usuario.dni = validated_data['dni']
    usuario.celular = validated_data['celular']
    usuario.email = validated_data['email']
    usuario.direccion = validated_data['direccion']
    usuario.usu_tipo = "cliente"

    usuario.save()
    return usuario


class UserEmpleadoSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  username = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=300)
  primerNombre = serializers.CharField(max_length=50)
  segundoNombre = serializers.CharField(max_length=50, required=False, allow_blank=True)
  apellidoPaterno = serializers.CharField(max_length=100)
  apellidoMaterno = serializers.CharField(max_length=100)
  dni = serializers.IntegerField()
  celular = serializers.IntegerField()
  email = serializers.CharField(max_length=100)
  direccion = serializers.CharField(max_length=100)
  usu_tipo = serializers.CharField(max_length=50)

  def create(self, validated_data):
    usuario = User()
        
    usuario.username = validated_data['username']
    usuario.set_password(validated_data['password'])
    usuario.primerNombre = validated_data['primerNombre']
    usuario.segundoNombre = validated_data['segundoNombre']
    usuario.apellidoPaterno = validated_data['apellidoPaterno']
    usuario.apellidoMaterno = validated_data['apellidoMaterno']
    usuario.dni = validated_data['dni']
    usuario.celular = validated_data['celular']
    usuario.email = validated_data['email']
    usuario.direccion = validated_data['direccion']
    usuario.usu_tipo = "administrador"

    usuario.save()
    return usuario

class ListarClienteSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  usuarios = UserEmpleadoSerializer()
  fechaNacimiento = serializers.DateField()
  distrito = serializers.CharField(max_length=100)
  fotoCliente = serializers.SerializerMethodField('get_fotoPerfil_path')
  

  def get_fotoPerfil_path(self, obj):
    return f"{servidor}/img/{obj.fotoCliente}"

class ClienteSerializer(serializers.Serializer):
  id = serializers.IntegerField()#usandolo en getClientes
  usuarios = UserEmpleadoSerializer()
  fechaNacimiento = serializers.DateField()
  distrito = serializers.CharField(max_length=100)
  fotoCliente = serializers.CharField(max_length=200)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)

class ClienteSaveSerializer(serializers.Serializer):
 
  usuarios = UserEmpleadoSerializer()
  fechaNacimiento = serializers.DateField()
  distrito = serializers.CharField(max_length=100)
  fotoCliente = serializers.CharField(max_length=200)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)


  def create(self, validated_data):
    cliente = Cliente()
    
    cliente.fechaNacimiento = validated_data['fechaNacimiento']
    cliente.distrito = validated_data['distrito']
    cliente.fotoCliente = validated_data['fotoCliente']
    usuarios = User.objects.filter(pk=validated_data['usuarios']['id']).last()
    
    cliente.usuarios = usuarios  

    cliente.save()
    return cliente
 
class ClienteDeleteSerializer(serializers.Serializer):
  
  def delete(self,queryset,validated_data):
    cliente = queryset

    cliente.estado = "I"
    cliente.fechaElimnado = datetime.now()
    
    cliente.save()
    return cliente

class ClienteUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  usuarios = UserEmpleadoSerializer()
  fechaNacimiento = serializers.DateField()
  distrito = serializers.CharField(max_length=100)
  fotoCliente = serializers.CharField(max_length=200)

  def update(self, queryset, validated_data):
    
    cliente = queryset
    
    cliente.fechaNacimiento = validated_data['fechaNacimiento']    
    cliente.distrito = validated_data['distrito']
    foto = validated_data['fotoCliente'].split('.io/img/')

    if(foto[0] == updatefile):
      cliente.fotoCliente = foto[1]
    else:
      cliente.fotoCliente = validated_data['fotoCliente']

    usuarios = User.objects.filter(pk=validated_data['usuarios']['id']).last()
    usuarios.fechaModificado = datetime.now()

    cliente.usuarios = usuarios  
    

    cliente.save()
    return cliente

class EmpleadoSerializer(serializers.Serializer):
  
  # id = serializers.IntegerField() para registrar un empleado no necesita id
  usuarios = UserEmpleadoSerializer()
  distrito = serializers.CharField(max_length=100)
  profesion = serializers.CharField(max_length=50)
  descripcion = serializers.CharField(max_length=200)
  fotoPerfil = serializers.CharField(max_length=200)
  fotoBanner = serializers.CharField(max_length=200)
  video = serializers.CharField(max_length=200)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)

  def create(self,validated_data):
    empleado = Empleado()

    empleado.distrito = validated_data['distrito']
    empleado.profesion = validated_data['profesion']
    empleado.descripcion = validated_data['descripcion']
    empleado.fotoPerfil = validated_data['fotoPerfil']
    empleado.fotoBanner = validated_data['fotoBanner']
    empleado.video = validated_data['video']
    usuarios = User.objects.filter(pk=validated_data['usuarios']['id']).last()
    
    empleado.usuarios = usuarios  
    empleado.save()
    return empleado
  

class ListarEmpleadoSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  usuarios = UserEmpleadoSerializer()
  distrito = serializers.CharField(max_length=100)
  profesion = serializers.CharField(max_length=50)
  descripcion = serializers.CharField(max_length=200)
  fotoPerfil = serializers.SerializerMethodField('get_fotoPerfil_path')
  fotoBanner = serializers.SerializerMethodField('get_fotoBanner_path')
  video = serializers.SerializerMethodField('get_video_path')

  def get_fotoPerfil_path(self, obj):
    return f"{servidor}/img/{obj.fotoPerfil}"

  def get_fotoBanner_path(self, obj):
    return f"{servidor}/img/{obj.fotoBanner}"

  def get_video_path(self, obj):
    return f"{servidor}/img/{obj.video}"

  def create(self,validated_data):
    empleado = Empleado()

    empleado.distrito = validated_data['distrito']
    empleado.profesion = validated_data['profesion']
    empleado.descripcion = validated_data['descripcion']
    empleado.fotoPerfil = validated_data['fotoPerfil']
    empleado.fotoBanner = validated_data['fotoBanner']
    empleado.video = validated_data['video']
    usuarios = User.objects.filter(pk=validated_data['usuarios']['id']).last()
    
    empleado.usuarios = usuarios  
    empleado.save()
    return empleado

class EmpleadoDeleteSerializer(serializers.Serializer):
  
  def delete(self,queryset,validated_data):
    empleado = queryset

    empleado.estado = "I"
    empleado.fechaElimnado = datetime.now()
    
    empleado.save()
    return empleado

class EmpleadoUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  usuarios = UserEmpleadoSerializer()
  distrito = serializers.CharField(max_length=100)
  profesion = serializers.CharField(max_length=50)
  descripcion = serializers.CharField(max_length=200)
  fotoPerfil = serializers.CharField(max_length=200)
  fotoBanner = serializers.CharField(max_length=200)
  video = serializers.CharField(max_length=200)

  def update(self, queryset, validated_data):

    empleado = queryset

    empleado.distrito = validated_data['distrito']
    empleado.profesion = validated_data['profesion']
    empleado.descripcion = validated_data['descripcion']
    foto = validated_data['fotoPerfil'].split('.io/img/')

    if(foto[0] == updatefile):
      empleado.fotoPerfil = foto[1]
    else:
      empleado.fotoPerfil = validated_data['fotoPerfil']

    banner = validated_data['fotoBanner'].split('.io/img/')
    if(banner[0] == updatefile):
      empleado.fotoBanner = banner[1]
    else:
      empleado.fotoBanner = validated_data['fotoBanner']

    vdeo = validated_data['video'].split('.io/img/')
    if(vdeo[0] == updatefile):
      empleado.video = vdeo[1]
    else:
      empleado.video = validated_data['video']    
    
    usuarios = User.objects.filter(pk=validated_data['usuarios']['id']).last()
    usuarios.fechaModificado = datetime.now()

    empleado.usuarios = usuarios  
    empleado.save()
    return empleado
    
class OfertaSerializer(serializers.Serializer):
  
  # id = serializers.IntegerField()
  empleado = ListarEmpleadoSerializer()
  fechaOferta = serializers.DateField()
  horaInicio = serializers.TimeField()
  horaFin = serializers.TimeField()
  costo = serializers.FloatField()
  estadoOferta = serializers.CharField(max_length=1)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)

class OfertaSaveSerializer(serializers.Serializer):
  
  # id = serializers.IntegerField()
  # empleado = serializers.ReadOnlyField(source='Empleado')
  empleado = ListarEmpleadoSerializer()
  fechaOferta = serializers.DateField()
  horaInicio = serializers.TimeField()
  horaFin = serializers.TimeField()
  costo = serializers.FloatField()
  # estadoOferta = serializers.CharField(max_length=1)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)
  

  def create(self,validated_data):
    oferta = Oferta()

    # oferta.empleado = validated_data['empleado']
    oferta.fechaOferta = validated_data['fechaOferta']
    oferta.horaInicio = validated_data['horaInicio']
    oferta.horaFin = validated_data['horaFin']
    oferta.costo = validated_data['costo']
    # oferta.estadoOferta = validated_data['estadoOferta']
    emplead = Empleado.objects.filter(pk=validated_data['empleado']['id']).last()
    
    oferta.empleado = emplead
  
    oferta.save()
    return oferta

  

 
class OfertaDeleteSerializer(serializers.Serializer):
  
  def delete(self,queryset,validated_data):
    oferta = queryset

    oferta.estado = "I"
    oferta.fechaElimnado = datetime.now()
    
    oferta.save()
    return oferta

class OfertaUpdateSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  empleado = ListarEmpleadoSerializer()
  fechaOferta = serializers.DateField()
  horaInicio = serializers.TimeField()
  horaFin = serializers.TimeField()
  costo = serializers.FloatField()
  estadoOferta = serializers.CharField(max_length=1)
  # fechaRegistro = serializers.DateField(required=False)
  # fechaModificado = serializers.DateField(required=False)
  # fechaElimnado = serializers.DateField(required=False)
  
  def update(self,queryset,validated_data):
    oferta = queryset

    oferta = queryset
    
    oferta.fechaOferta = validated_data['fechaOferta']
    oferta.horaInicio = validated_data['horaInicio']
    oferta.horaFin = validated_data['horaFin']
    oferta.costo = validated_data['costo']    
    oferta.fechaModificado = datetime.now()
    emplead = Empleado.objects.filter(pk=validated_data['empleado']['id']).last()
    
    oferta.empleado = emplead
    
    oferta.save()
    return oferta
  
class CarritoSerializer(serializers.Serializer):
  
  # id = serializers.IntegerField()
  cliente = ClienteSerializer()
  estadoCarrito = serializers.CharField(max_length=1)
  estado = serializers.CharField(max_length=1)
  fechaRegistro = serializers.DateField(required=False)
  fechaModificado = serializers.DateField(required=False)
  fechaElimnado = serializers.DateField(required=False)
  ofertas = OfertaSerializer(many=True)
 
class CarritoSaveSerializer(serializers.Serializer):

  cliente = ClienteSerializer()  
  ofertas = serializers.ListField()

  def create(self,validated_data):
    carrito = Carrito()
        
    cliente = Cliente.objects.filter(pk=validated_data['cliente']['id']).last()
    
    carrito.cliente = cliente  
    
    for item in validated_data['ofertas']:
      
      oferta = Oferta.objects.filter(pk=item["id"]).last()
      print(oferta.id)
      # if oferta == None:
      #   oferta = Oferta()
      #   oferta.id=item["id"]
      #   oferta.save()
      
      carrito.ofertas.add(oferta)
    
    carrito.save()
    return carrito