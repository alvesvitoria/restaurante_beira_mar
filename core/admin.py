from django.contrib import admin
from .models import Cardapio, Mesa, Reserva


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_prato']
    list_display_links = list_display


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = list_display


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'mesa']
    list_display_links = list_display


