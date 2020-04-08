from django.urls import path
from django.conf.urls import url,include
from .views import *
from cliente import views
app_name = "cliente"


urlpatterns = [
   	path("registro-cliente/", views.RegistroCliente.as_view(), name="registro_cliente"),
   	path("iniciar-sesion-cliente/", views.InicioSesion.as_view(), name="inicio_sesion_cliente"),

]
