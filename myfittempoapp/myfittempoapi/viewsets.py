from rest_framework import viewsets
from myfittempoapi.serializer import ClienteSerializer
from myfittempoapi.models import Cliente
from rest_framework.response import Response

class ClienteViewset(viewsets.ViewSet):

  def listar(self,request):    
    queryset = Cliente.objects.all()
    serializer = ClienteSerializer(queryset, many=True)
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