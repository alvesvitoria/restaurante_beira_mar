from django.db import models
from accounts.models import Cliente


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
        return str(self.id)

    class Meta:
        db_table = 'cardapio'


class Mesa(models.Model):
    num_mesa = models.IntegerField()
    quant_cadeiras = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'mesa'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    data = models.DateField()
    periodo = models.DurationField()
    quant_pessoas = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'reservas'


class Promocao(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    desconto = models.FloatField()
    cardapio = models.ForeignKey(Cardapio, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'promocao'
