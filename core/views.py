from django.db.models.query_utils import Q
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cardapio, Mesa, Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest):
    return render(request, 'core/index.html')


def cardapio_detail(request: HttpRequest, id):
    cardapio = Cardapio.objects.get(ativo=True, id=id)

    return render(request, 'core/cardapio.html', {'cardapio': cardapio})


def list_all_cardapio(request: HttpRequest):
    cardapios = Cardapio.objects.filter(ativo=True)
    return render(request, 'core/list-cardapio.html', {'cardapios': cardapios})


@login_required(login_url='accounts:login')
def reserva(request: HttpRequest):
    # https://docs.djangoproject.com/en/3.2/topics/db/sql/#index-lookups
    mesa_livre = Mesa.objects.raw('''
        SELECT * FROM mesa WHERE
            NOT mesa.id IN (SELECT reserva.mesa_id FROM reserva)
            LIMIT 1;
    ''')
    if not mesa_livre:
        messages.error(request, 'Sem mesas disponíveis.')
        return redirect('core:index')

    form = None

    if request.method != 'POST':
        form = ReservaForm()
    else:
        form = ReservaForm(data=request.POST)

        if form.is_valid():
            # https://django-portuguese.readthedocs.io/en/1.0/topics/forms/modelforms.html#usando-somente-alguns-campos-no-formulario
            rsv = form.save(commit=False)

            rsv.cliente = request.user
            rsv.mesa = mesa_livre[0]

            rsv.save()
            messages.success(request, 'Reserva feita com sucesso.')
            return redirect('core:index')

    return render(request, 'core/reserva.html', {'form': form})


@login_required(login_url='accounts:login')
def cancela_reserva(request: HttpRequest, id):
    Reserva.objects.get(pk=id).delete()
    messages.success(request, 'Reserva cancelada com sucesso.')
    return redirect('accounts:dashboard')


def contato(request: HttpRequest):
    return render(request, 'core/contato.html')
