from myfittempoapi.serializer import UserClienteSerializer
from myfittempoapi.serializer import ListarEmpleadoSerializer
from os import pardir
from rest_framework import viewsets
from myfittempoapi.serializer import ClienteSerializer,EmpleadoSerializer,OfertaSerializer,CarritoSerializer,CarritoSaveSerializer,ClienteUpdateSerializer,EmpleadoUpdateSerializer,OfertaUpdateSerializer,UserEmpleadoSerializer,UserSerializer,OfertaSaveSerializer,OfertaDeleteSerializer
from myfittempoapi.models import Cliente, Empleado, Oferta, Carrito,User
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from myfittempoapi.lib.mercadopago import MercadoPago

ACCESS_TOKEN = "TEST-6632320225707807-061720-81951e5b1d7ba9fd8aacc23d2548785c-777281793"
mp = MercadoPago(access_token=ACCESS_TOKEN)

# class TokenizeViewset(viewsets.ViewSet):

#   def get_token(self, request):
#     data = request.data
#     try:
#       user = User.objects.get(username=data["user"])
#       if user.check_password(data["password"]):
#         try:
#           token = Token.objects.get(user=user)
#         except:
#           token = Token.objects.create(user=user)

#         return Response({
#           "token": token.key
#         })
#       else:
#         return Response({
#         "status":"unauthorized 1"
#         })
#     except:
#       return Response({
#         "status":"unauthorized 2"
#         })
class VerificarTokenViewset(viewsets.ViewSet):
   pass

class UsuarioViewset(viewsets.ViewSet):
  
  def create(self, request):
    data = request.data
    serializer = UserSerializer(data=data)
    #ahora toca validar / is_valid devuelve un binario 
    if serializer.is_valid():      
      serializer.save()#va llamar al metodo create del zerializer
      reponse = {
        "status": serializer.is_valid()
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def create_usu_cliente(self, request):
    data = request.data
    serializer = UserClienteSerializer(data=data)
    #ahora toca validar / is_valid devuelve un binario 
    if serializer.is_valid():      
      serializer.save()#va llamar al metodo create del zerializer
      reponse = {
        "status": serializer.is_valid()
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def listar(self,request):
  
    queryset = User.objects.all()
    serializer = UserEmpleadoSerializer(queryset, many=True)
    return Response(serializer.data)

  def listar_usuario_activo(self,request):
  
    queryset = User.objects.filter(usu_tipo='colaborador')
    serializer = UserEmpleadoSerializer(queryset, many=True)
    return Response(serializer.data)
  
class ClienteViewset(viewsets.ViewSet):
 
  def update(self,request,id):
    queryset = Cliente.objects.get(pk=id)    
    data = request.data
    serializer = ClienteUpdateSerializer(data=data)
    if serializer.is_valid():
      serializer.update(queryset, serializer.validated_data)
      return Response({"status": "ok"})
    else:
      return(Response({
        "errors": serializer.errors
      }))
  
  def listar(self,request):
    #  user = request.user
    # queryset = Cliente.objects.filter(owner=user)
    queryset = Cliente.objects.all()
    serializer = ClienteSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self,request, id):
    queryset = Cliente.objects.get(pk=id)
    serializer = ClienteSerializer(queryset)
    return Response(serializer.data)

  def create(self, request):
    data = request.data
    serializer = ClienteSerializer(data=data)
    #ahora toca validar / is_valid devuelve un binario 
    if serializer.is_valid():
      serializer.save()      
      reponse = {
        "status": serializer.is_valid()        
      }
      return Response(reponse)
    else:
      return(Response({
        "error": serializer.errors
      }))

class EmpleadoUsuarioViewset(viewsets.ViewSet):
  
  def listar_empleado_id_usuario(self, request,id):
    user = User.objects.get(pk=id)
    queryset = Empleado.objects.filter(usuarios=user)
    serializer = EmpleadoSerializer(queryset, many=True)
    return Response(serializer.data)

class EmpleadoViewset(viewsets.ViewSet):

  def update(self,request,id):
    queryset = Empleado.objects.get(pk=id)
    data = request.data
    serializer = EmpleadoUpdateSerializer(data=data)
    if serializer.is_valid():
      serializer.update(queryset, serializer.validated_data)
      return Response({"status": "ok"})
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def listar(self,request):
    
    queryset = Empleado.objects.all()
    serializer = ListarEmpleadoSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self,request, id):
    queryset = Empleado.objects.get(pk=id)
    serializer = EmpleadoSerializer(queryset)
    return Response(serializer.data)

  def create(self, request):
    data = request.data    
    serializer = EmpleadoSerializer(data=data)
    #ahora toca validar / is_valid devuelve un binario 
    if serializer.is_valid():      
      serializer.save()#va llamar al metodo create del zerializer
           
      reponse = {
        "status": serializer.is_valid(),
        "content": serializer.data
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))

  # def create(self, request):
  #   data = request.data
  #   serializer = EmpleadoSerializer(data=data)
  #   #ahora toca validar / is_valid devuelve un binario 
  #   if serializer.is_valid():      
  #     serializer.save()#va llamar al metodo create del zerializer
  #     reponse = {
  #       "status": serializer.is_valid()
  #     }
  #     return Response(reponse)
  #   else:
  #     return(Response({
  #       "errors": serializer.errors
  #     }))

class OfertaViewset(viewsets.ViewSet):
  
  
  def delete(self,request,id):
    queryset = Oferta.objects.get(pk=id)
    data = request.data
    serializer = OfertaDeleteSerializer(data=data)
    if serializer.is_valid():
      # print(queryset)
      serializer.delete(queryset, serializer.validated_data)
      return Response({"status": "ok"})
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def update(self,request,id):
    queryset = Oferta.objects.get(pk=id)
    data = request.data
    serializer = OfertaUpdateSerializer(data=data)
    if serializer.is_valid():
      # print(queryset)
      serializer.update(queryset, serializer.validated_data)
      return Response({"status": "ok"})
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def listar_oferta_por_trabajador(self, request,id):    
    user = User.objects.get(pk=id)
    empleado = Empleado.objects.get(usuarios=user.id)   
    queryset = Oferta.objects.filter(empleado=empleado, estadoOferta="A")
    serializer = OfertaUpdateSerializer(queryset, many=True)
    return Response(serializer.data)
 
  def listar_activos(self,request):
    queryset = Oferta.objects.filter(estadoOferta="A")
    serializer = OfertaSerializer(queryset, many=True)
    return Response(serializer.data)

  def listar(self,request):  
    queryset = Oferta.objects.all()
    serializer = OfertaSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self,request, id):
    queryset = Oferta.objects.get(pk=id)
    serializer = OfertaSerializer(queryset)
    return Response(serializer.data)
    
  def create(self, request):
    data = request.data
    # print(data)
    serializer = OfertaSaveSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      reponse = {
        "status": serializer.is_valid()
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))

class MercadopagoViewset(viewsets.ViewSet):

  def create(self, request):
    data = request.data    
    items=[]
    for product in data:
      ofert ={}
      ofert['title'] = "Sesión desde " + str(product['horaInicio']) + " hasta " + str(product['horaFin'])
      ofert['description'] = "Con "+ product['empleado']['usuarios']['primerNombre'] + " " + product['empleado']['usuarios']['apellidoPaterno'] + " " + product['empleado']['usuarios']['apellidoMaterno']
      ofert['currency_id'] = 'PEN'
      ofert['quantity'] = 1
      ofert['unit_price'] = product['costo']
      ofert['back_urls'] = {"success": "http://localhost:3000",
        "failure": "http://localhost:3000",
        "pending": "http://localhost:3000"}
      ofert['auto_return'] = "all"
      items.append(ofert)

    preference_data = {
        "items": items
      }
    
    preference = mp.create_preference(data=preference_data)
    rpt = preference["sandbox_init_point"]    
    return Response({'rpt':rpt})

class CarritoViewset(viewsets.ViewSet):
  
  def listar(self,request):
    queryset = Carrito.objects.all()    
    serializer = CarritoSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self,request, id):
    queryset = Carrito.objects.get(pk=id)
    serializer = CarritoSerializer(queryset)
    return Response(serializer.data)
    
  def create(self, request):
    data = request.data
    serializer = CarritoSaveSerializer(data=data)

    if serializer.is_valid():
      serializer.save()
      reponse = {
        "status": serializer.is_valid()
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))