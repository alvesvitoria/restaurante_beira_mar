from django.contrib import admin
from .models import Clientes
from .models import Cardapio

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nm_cliente']


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nm_prato']