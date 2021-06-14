from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    form = None
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth.login(request, user)
                return redirect('accounts:dashboard')

    return render(request, 'accounts/login.html', {'form': form})


@login_required(redirect_field_name='accounts:login')
def logout(request: HttpRequest):
    auth.logout(request)
    return redirect('post:index')


def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado com sucesso. Faça login.')
            return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form': form})


@login_required(redirect_field_name='accounts:login')
def dashboard(request: HttpRequest):
    return render(request, 'accounts/dashboard.html')
