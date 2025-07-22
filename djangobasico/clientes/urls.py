from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # A url "clientes" redireciona pra cá
]