from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Clientes
from django.contrib.auth import logout


# Create your views here.
def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def list_all_cliente(request):
    cliente = Clientes.objects.filter(active=True)
    return render(request, 'list.html', {'cliente': cliente})


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