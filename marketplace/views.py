from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Anuncio, ProdutoImagem
from django.core.paginator import Paginator



@login_required
def cadastro_item_view(request):

    categorias = Categoria.objects.all()

    if request.method == 'POST':

        imagens = request.FILES.getlist('imagens')

        if len(imagens) > 5:

            return render(
                request,
                'cadastro_item.html',
                {
                    'categorias': categorias,
                    'erro': 'Você pode cadastrar no máximo 5 imagens.'
                }
            )

        produto = Produto.objects.create(
            nome_produto=request.POST.get('nome_produto'),
            modelo=request.POST.get('modelo'),
            ano=request.POST.get('ano'),
            serie=request.POST.get('serie'),
            raridade=request.POST.get('raridade'),
            desc_produto=request.POST.get('descricao'),
            categoria_id=request.POST.get('categoria'),
            usuario=request.user
        )

        for imagem in imagens:

            ProdutoImagem.objects.create(
                produto=produto,
                imagem=imagem
            )

        return redirect('perfil')
    
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

@login_required
def anuncio_view(request, id):

    anuncio = get_object_or_404(
        Anuncio.objects.select_related(
            'produto',
            'produto__categoria',
            'usuario'
        ).prefetch_related(
            'produto__imagens'
        ),
        id=id
    )

    return render(
        request,
        'anuncio.html',
        {
            'anuncio': anuncio
        }
    )

@login_required
def editar_anuncio_view(request, id):

    anuncio = get_object_or_404(
        Anuncio.objects.select_related('produto'),
        id=id
    )

    if anuncio.usuario != request.user:
        return redirect('anunciados')

    if request.method == 'POST':

        anuncio.preco = request.POST.get('preco')
        anuncio.descricao = request.POST.get('descricao')

        anuncio.save()

        return redirect('anuncio', id=anuncio.id)

    return render(request, 'editar_anuncio.html', {
        'anuncio': anuncio
    })

@login_required
def vender_anuncio(request, id):

    anuncio = get_object_or_404(Anuncio, id=id)

    if anuncio.usuario != request.user:
        return redirect('anunciados')

    anuncio.status = 'VENDIDO'
    anuncio.save()

    return redirect('anuncio', id=anuncio.id)
