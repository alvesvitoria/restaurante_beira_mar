from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')


# Create your views here.
def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')



@login_required(login_url='/login/')
def set_cardapio(request):
    nm_prato = request.POST.get('nm_prato')
    tamanho = request.POST.get('tamanho')
    categoria = request.POST.get('categoria')
    ingredientes = request.POST.get('ingredientes')
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')
    file = request.FILES.get('file')
    user = request.user
    cardapio_id = request.POST.get('cardapio_id')
    if cardapio_id:
        cardapio = Cardapio.objects.get(id=cardapio_id)
        if user == cardapio.user:
            cardapio.nm_prato = nm_prato
            cardapio.categoria = categoria
            cardapio.descricao = descricao
            if file:
                cardapio.photo = file
                cardapio.save()
    else:
        cardapio = Cardapio.objects.create(nm_prato=nm_prato, categoria=categoria, descricao=descricao, user=user, photo=file)
        url = '/cardapio/detail/{}/'.format(cardapio.id)
    return redirect(url)



def cardapio_detail(request, id):
    cardapio = Cardapio.objects.get(active=True, id=id)
    return render(request, 'cardapio.html', {'cardapio':cardapio})


def list_all_cardapio(request):
    cardapio = Cardapio.objects.filter(active=True)
    return render(request, 'list-cardapio.html', {'cardapio':cardapio})



