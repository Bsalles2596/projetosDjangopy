from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Salvar dados do Front no BD
    novo_usuario = Usuario()
    novo_usuario.login = request.POST.get('login')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()

# Exibir todos Usuarios do front ja cadastrados no BD em uma nova pagina   

    usuarios = {
    'usuarios': Usuario.objects.all()

    }

# Retornar dados para pagina de listagem de usuarios

    return render(request,'usuarios/usuarios.html',usuarios)