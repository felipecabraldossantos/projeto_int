from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Anuncio
from django.core.paginator import Paginator


def home_view(request):
    return render(request, 'home.html')

@login_required
def cadastro_item_view(request):

    if request.method == 'POST':

        Produto.objects.create(
            nome_produto=request.POST.get('nome_produto'),
            modelo=request.POST.get('modelo'),
            ano=request.POST.get('ano'),
            serie=request.POST.get('serie'),
            raridade=request.POST.get('raridade'),
            desc_produto=request.POST.get('descricao'),
            categoria_id=request.POST.get('categoria'),
            usuario=request.user
        )

        return redirect('perfil')

    categorias = Categoria.objects.all()

    return render(
        request,
        'cadastro_item.html',
        {
            'categorias': categorias
        }
    )

@login_required
def inventario_view(request):

    produtos = Produto.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        'inventario.html',
        {
            'produtos': produtos
        }
    )

@login_required
def cadastro_anuncio_view(request):

    if request.method == 'POST':

        produto = Produto.objects.get(
            id=request.POST.get('produto')
        )

        Anuncio.objects.create(
            produto=produto,
            usuario=request.user,
            preco=request.POST.get('preco'),
            descricao=request.POST.get('descricao'),
            status='ATIVO'
        )

        return redirect('perfil')

    produtos = Produto.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        'cadastro_anuncio.html',
        {
            'produtos': produtos
        }
    )

def anunciados_view(request):

    anuncios = Anuncio.objects.filter(
        status='ATIVO'
    ).order_by('-data_publicacao')

    paginator = Paginator(anuncios, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'anunciados.html',
        {
            'page_obj': page_obj
        }
    )
