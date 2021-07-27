from myfittempoapi.models import Cliente
from myfittempoapi.serializer import ClienteSaveSerializer
from myfittempoapi.serializer import EmpleadoSerializer
from rest_framework.views import APIView
from myfittempoapi.models import Empleado
from rest_framework.response import Response

class EmpleadoImagenController(APIView):
  def post(self, request):
    file = request.FILES["imagen"]
    fileBanner = request.FILES["banner"]
    fileVideo = request.FILES["video"]
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)
    empleado.fotoPerfil=file
    empleado.fotoBanner=fileBanner
    empleado.video=fileVideo
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    

    return Response({
      "ok":True,
      "content": serializer.data
    })

class ClienteImagenControllerPerfil(APIView):
  def post(self, request):
    file = request.FILES["imagen"]    
    cliente_id = request.POST["id"]
    
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.fotoCliente=file    
    cliente.save()

    serializer = ClienteSaveSerializer(cliente)

    return Response({
      "ok":True,
      "content": serializer.data
    })

class EmpleadoImagenControllerPerfil(APIView):
  def post(self, request):
    file = request.FILES["imagen"]    
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)
    empleado.fotoPerfil=file    
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })

class EmpleadoImagenControllerBanner(APIView):
  def post(self, request):    
    fileBanner = request.FILES["banner"]    
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)    
    empleado.fotoBanner=fileBanner   
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })

class EmpleadoImagenControllerVideo(APIView):
  def post(self, request):    
    fileVideo = request.FILES["video"]
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)    
    empleado.video=fileVideo
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })

class EmpleadoImagenControllerPerfilBanner(APIView):
  def post(self, request):
    file = request.FILES["imagen"]
    fileBanner = request.FILES["banner"]    
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)
    empleado.fotoPerfil=file
    empleado.fotoBanner=fileBanner  
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })

class EmpleadoImagenControllerPerfilVideo(APIView):
  def post(self, request):
    file = request.FILES["imagen"]    
    fileVideo = request.FILES["video"]
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)
    empleado.fotoPerfil=file 
    empleado.video=fileVideo
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })
class EmpleadoImagenControllerBannerVideo(APIView):
  def post(self, request):    
    fileBanner = request.FILES["banner"]
    fileVideo = request.FILES["video"]
    empleado_id = request.POST["id"]
    
    empleado = Empleado.objects.get(pk=empleado_id)    
    empleado.fotoBanner=fileBanner
    empleado.video=fileVideo
    empleado.save()

    serializer = EmpleadoSerializer(empleado)

    return Response({
      "ok":True,
      "content": serializer.data
    })
    