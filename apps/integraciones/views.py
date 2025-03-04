from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def integraciones_home(request):
    return HttpResponse("Bienvenido a la sección de integraciones")
