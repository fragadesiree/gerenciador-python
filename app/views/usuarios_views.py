from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render


def cadastrar_usuarios(request):
    if request.method == "POST":
        form_usuarios = UserCreationForm(request.POST)
        if form_usuarios.is_valid():
            form_usuarios.save()
            return redirect('listar_tarefas')
    else:
            form_usuarios = UserCreationForm()
    return render(request, 'usuarios/form_usuarios.html', {"form_usuarios": form_usuarios})


def logar_usuarios(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'Login ou sennha inválidos')
            return redirect('logar_usuarios')
    else:
        form_login = AuthenticationForm()
        return render(request, 'usuarios/login.html', {"form_login": form_login})


def deslogar_usuarios(request):
    logout(request)
    return redirect('logar_usuarios')