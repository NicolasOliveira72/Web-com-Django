from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'nome': 'José Silva',
        'idade': 25,
        'produtos': [
            {'nome': 'notebook', 'preco': '1.200,00'},
            {'nome': 'celular', 'preco': '900,00'},
            {'nome': 'tablet', 'preco': '800,00'},
        ]
    }

    return render(request, 'index.html', context)

def celulares(request):
    return render(request, 'celulares.html')

def moveis(request):
    return render(request, 'moveis.html')
