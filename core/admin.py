from django.contrib import admin
from .models import Clientes


@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nm_cliente']