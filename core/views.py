from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'core/index.html')


# @login_required(login_url='/login/')
# def set_cardapio(request):
#     nm_prato = request.POST.get('nm_prato')
#     tamanho = request.POST.get('tamanho')
#     categoria = request.POST.get('categoria')
#     ingredientes = request.POST.get('ingredientes')
#     valor = request.POST.get('valor')
#     descricao = request.POST.get('descricao')
#     file = request.FILES.get('file')
#     user = request.user
#     cardapio_id = request.POST.get('cardapio_id')
#     if cardapio_id:
#         cardapio = Cardapio.objects.get(id=cardapio_id)
#         if user == cardapio.user:
#             cardapio.nm_prato = nm_prato
#             cardapio.categoria = categoria
#             cardapio.descricao = descricao
#             if file:
#                 cardapio.photo = file
#                 cardapio.save()
#     else:
#         cardapio = Cardapio.objects.create(nm_prato=nm_prato, categoria=categoria, descricao=descricao, user=user, photo=file)
#         url = '/cardapio/detail/{}/'.format(cardapio.id)
#     return redirect(url)


def cardapio_detail(request, id):
    cardapio = Cardapio.objects.get(ativo=True, id=id)
    return render(request, 'core/cardapio.html', {'cardapio': cardapio})


def list_all_cardapio(request):
    cardapio = Cardapio.objects.filter(ativo=True)
    return render(request, 'core/list-cardapio.html', {'cardapio': cardapio})
