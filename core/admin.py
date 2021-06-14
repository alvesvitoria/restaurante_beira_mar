from django.contrib import admin
from .models import Cardapio, Mesa, Promocao, Reserva


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_prato']


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['id', 'quant_cadeiras']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data', 'periodo', 'quant_pessoas']


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ativo', 'nome', 'desconto']
