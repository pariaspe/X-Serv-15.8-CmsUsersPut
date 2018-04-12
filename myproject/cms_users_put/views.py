from django.shortcuts import render
from django.http import HttpResponse

from .models import Pages

# Create your views here.
def barra(request):
    return HttpResponse('Hola')

def otro(request, recurso):
    return HttpResponse('El recurso es ' + recurso)
