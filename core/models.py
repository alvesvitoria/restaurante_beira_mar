from accounts.models import Cliente
from django.db import models


class Cardapio(models.Model):
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types
    class Categorias(models.TextChoices):
        ARABE = 'Árabe'
        ORIENTAL = 'Oriental'
        BRASILEIRA = 'Brasileira'
        MEDITERRANEA = 'Mediterrânea'
        CONTEMPORANEA = 'Contemporânea'
        __empty__ = 'Desconhecido'

    nome_prato = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=11)
    categoria = models.CharField(
        default=Categorias.__empty__, max_length=15, choices=Categorias.choices)
    ingredientes = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='prato', blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_prato

    class Meta:
        db_table = 'cardapio'


class Mesa(models.Model):
    num_mesa = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.num_mesa)

    class Meta:
        db_table = 'mesa'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, default=None)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, default=None)
    data = models.DateField()
    hora = models.TimeField(default=None)

    def __str__(self):
        return f'{self.cliente} / {self.mesa}'

    class Meta:
        db_table = 'reserva'
