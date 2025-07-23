from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'nome': 'José Silva'
    }

    return render(request, 'index.html', context)

def celulares(request):
    return render(request, 'celulares.html')
