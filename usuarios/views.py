from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required



def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('perfil')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        Usuario.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        return redirect('login')

    return render(request, 'cadastro.html')

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')