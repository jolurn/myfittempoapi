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