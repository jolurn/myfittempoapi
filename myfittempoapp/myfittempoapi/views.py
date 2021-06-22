from myfittempoapi.models import Cliente
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.


def hello_world(request):
  pass
  # cliente = Cliente.objects.all()
  # data = serializers.serialize("xml",cliente)
  # print(data)
  # return HttpResponse(data)