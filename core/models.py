from django.db import models
from django.contrib.auth.models import User


class Clientes(models.Model):
    nm_cliente = models.CharField(max_length=150)
    endereco = models.TextField()
    telefone = models.CharField(max_length=11)
    celular = models.CharField(max_length=11)
    email = models.EmailField()
    cpf = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'clientes'


class Cardapio(models.Model):
    nm_prato = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=11)
    categoria = models.CharField(max_length=50)
    ingredientes = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    photo = models.ImageField(upload_to='prato', blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


    class Meta:
        db_table = 'cardapio'


class Reserva(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=13)
    ocasiao = models.CharField(max_length=60)
    num_pessoas = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'reservas'


class Mesa(models.Model):
    num_mesa = models.IntegerField()
    quant_cadeiras = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'mesa'


class Horario(models.Model):
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    id_reservas = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'horario'