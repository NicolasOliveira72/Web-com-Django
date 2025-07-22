from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def tela_inicial(request):
    return HttpResponse('Bem vindo a tela de inicio')