
from django.http.response import HttpResponse
from myfittempoapi.models import User,Empleado
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from myfittempoapi.serializer import CustomObtainPairSerializer
from rest_framework.response import Response

# Create your views here.

class LoginAPI(APIView):
    def post(self, request):
        login_data = request.data        
        email = login_data["correo"]
        user = User.objects.filter(email__exact=email).first()        
        password = login_data.get("password")
        user_authenticated = authenticate(username=user.username, password=password)
        if user_authenticated != None:
                        
            token = CustomObtainPairSerializer.get_token(user_authenticated)

            return Response({
                'ok': True,
                'token': str(token),
                'usu_tipo': str(user.usu_tipo),
                'id': str(user.id),                
            })
            

        
        return HttpResponse("ok")