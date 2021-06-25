from accounts.models import ClienteManager
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cardapio
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest):
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


def cardapio_detail(request: HttpRequest, id):
    cardapio = Cardapio.objects.get(ativo=True, id=id)
    return render(request, 'core/cardapio.html', {'cardapio': cardapio})


def list_all_cardapio(request: HttpRequest):
    cardapio = Cardapio.objects.filter(ativo=True)
    return render(request, 'core/list-cardapio.html', {'cardapio': cardapio})


@login_required
def reserva(request: HttpRequest):
    form = None
    
    if request.method != 'POST':
        form = ReservaForm()
    else:
        form = ReservaForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Reserva feita com sucesso.')
            form.save()
            return redirect('core:index')

    return render(request, 'core/reserva.html', {'form': form})

    
