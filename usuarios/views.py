from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from marketplace.models import Produto, Anuncio


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
        whatsapp = request.POST.get('whatsapp')

        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar_senha')

        if senha != confirmar:
            return render(request, 'cadastro.html', {
                'erro': 'As senhas não coincidem.'
            })

        if Usuario.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {
                'erro': 'Este nome de usuário já está em uso.'
            })

        if Usuario.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {
                'erro': 'Este e-mail já está cadastrado.'
            })

        Usuario.objects.create_user(
            username=username,
            email=email,
            password=senha,
            whatsapp=whatsapp
        )

        return redirect('login')

    return render(request, 'cadastro.html')

@login_required
def perfil_view(request):

    total_itens = Produto.objects.filter(
        usuario=request.user
    ).count()

    total_anuncios = Anuncio.objects.filter(
        usuario=request.user
    ).count()

    ultimos_anuncios = Anuncio.objects.filter(
        usuario=request.user
    ).order_by('-id')[:4]

    return render(
        request,
        'perfil.html',
        {
            'total_itens': total_itens,
            'total_anuncios': total_anuncios,
            'ultimos_anuncios': ultimos_anuncios,
        }
    )