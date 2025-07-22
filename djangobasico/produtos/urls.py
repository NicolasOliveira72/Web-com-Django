from django.urls import path 
from . import views

urlpatterns = [
    path('', views.pagina_produtos ), # A url "produto" redireciona pra cá
    path('celulares', views.pagina_celulares),
]
