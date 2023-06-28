
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota , view responsabel , nome de referencia 
    # usuarios.com
    path('', views.home,name= 'home'),
    # usuarios.com/usuarios
    path('usuario/', views.usuarios,name='lista_de_usuarios'),
]
