from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')


admin.site.register(Cliente, UserAdmin)
# admin.site.unregister(Group)
