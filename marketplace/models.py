from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=30)
    desc_categoria = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nome_categoria
    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    modelo = models.CharField(max_length=30)
    ano = models.IntegerField()
    serie = models.CharField(max_length=30)
    raridade = models.CharField(max_length=30)
    desc_produto = models.CharField(max_length=100)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome_produto
    
class Anuncio(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    descricao = models.TextField()

    status = models.CharField(
        max_length=10,
        default='ATIVO'
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    data_publicacao = models.DateTimeField(
        auto_now_add=True
    )

class Favorito(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    anuncio = models.ForeignKey(
        Anuncio,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'favorito'
        unique_together = ('usuario', 'anuncio')

class Avaliacao(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    anuncio = models.ForeignKey(
        Anuncio,
        on_delete=models.CASCADE
    )

    avaliacao = models.IntegerField()

    class Meta:
        db_table = 'avaliacao'

class ProdutoImagem(models.Model):

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='imagens'
    )

    imagem = models.ImageField(
        upload_to='produtos/'
    )

    def __str__(self):
        return f'Imagem de {self.produto.nome_produto}'

