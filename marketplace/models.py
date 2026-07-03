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
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data_publicacao = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(max_length=7)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'anuncio'

    def __str__(self):
        return self.titulo
    
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
