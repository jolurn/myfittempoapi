from myfittempoapi.models import Cliente
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.

def login(request):
  if request.method == "GET":
    return render(request, "login.html",{"flag": False})
  else:
    data = request.POST

    try:
      user = User.objects.get(username=data["user"])

      if user.check_password(data["password"]):
        return HttpResponse("ok")
      else:
        return render(request, "login.html",{"flag":True})
    except:
      return render(request, "login.html",{"flag":True})

def hello_world(request):
  pass
  # cliente = Cliente.objects.all()
  # data = serializers.serialize("xml",cliente)
  # print(data)
  # return HttpResponse(data)