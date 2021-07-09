from os import pardir
from rest_framework import viewsets
from myfittempoapi.serializer import ClienteSerializer,EmpleadoSerializer,OfertaSerializer,CarritoSerializer,CarritoSaveSerializer,ClienteUpdateSerializer,EmpleadoUpdateSerializer,OfertaUpdateSerializer
from myfittempoapi.models import Cliente, Empleado, Oferta, Carrito
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from myfittempoapi.lib.mercadopago import MercadoPago

ACCESS_TOKEN = "TEST-6632320225707807-061720-81951e5b1d7ba9fd8aacc23d2548785c-777281793"
mp = MercadoPago(access_token=ACCESS_TOKEN)

class TokenizeViewset(viewsets.ViewSet):

  def get_token(self, request):
    data = request.data
    try:
      user = User.objects.get(username=data["user"])
      if user.check_password(data["password"]):
        try:
          token = Token.objects.get(user=user)
        except:
          token = Token.objects.create(user=user)

        return Response({
          "token": token.key
        })
      else:
        return Response({
        "status":"unauthorized 1"
        })
    except:
      return Response({
        "status":"unauthorized 2"
        })

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

class EmpleadoViewset(viewsets.ViewSet):
  # authentication_classes = [BasicAuthentication,]
  # permission_classes = [IsAuthenticated,]

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
    serializer = EmpleadoSerializer(queryset, many=True)
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
        "status": serializer.is_valid()
      }
      return Response(reponse)
    else:
      return(Response({
        "errors": serializer.errors
      }))

class OfertaViewset(viewsets.ViewSet):
  
  def update(self,request,id):
    queryset = Oferta.objects.get(pk=id)
    data = request.data
    serializer = OfertaUpdateSerializer(data=data)
    if serializer.is_valid():
      serializer.update(queryset, serializer.validated_data)
      return Response({"status": "ok"})
    else:
      return(Response({
        "errors": serializer.errors
      }))

  def listar_oferta_por_trabajador(self, request):    
    user = request.user
    queryset = Oferta.objects.filter(owner=user)
    serializer = OfertaSerializer(queryset, many=True)
    return Response(serializer.data)

  def listar(self,request):  
    queryset = Oferta.objects.all()
            
    # for product in queryset:     
    #   preference_data = {
    #     "items": [{
    #       "title": "Sesión desde " + str(product.horaInicio) + " hasta " + str(product.horaFin),
    #       "description": "Con "+ product.empleado.primerNombre + " " + product.empleado.apellidoPaterno + " " + product.empleado.apellidoMaterno,
    #       "currency_id": "PEN",
    #       "quantity": 1,
    #       "unit_price": product.costo
    #     }]
    #   }
    #   preference = mp.create_preference(data=preference_data)
    #   product.init_point = preference["sandbox_init_point"]
           
    serializer = OfertaSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self,request, id):
    queryset = Oferta.objects.get(pk=id)
    serializer = OfertaSerializer(queryset)
    return Response(serializer.data)
    
  def create(self, request):
    data = request.data
    serializer = OfertaSerializer(data=data)

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
      ofert['description'] = "Con "+ product['empleado']['primerNombre'] + " " + product['empleado']['apellidoPaterno'] + " " + product['empleado']['apellidoMaterno']
      ofert['currency_id'] = 'PEN'
      ofert['quantity'] = 1
      ofert['unit_price'] = product['costo']
      items.append(ofert)

    preference_data = {
        "items": items
      }
    print(preference_data)
    preference = mp.create_preference(data=preference_data)
    rpt = preference["sandbox_init_point"]
    # print(preference)
    return Response({'rpt':rpt})

class CarritoViewset(viewsets.ViewSet):
  
  def listar(self,request):
    queryset = Carrito.objects.all()
    print(queryset)
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