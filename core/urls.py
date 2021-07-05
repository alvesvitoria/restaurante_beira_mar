from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('cardapios/', views.list_all_cardapio, name='cardapios'),
    path('cardapio/<int:id>/', views.cardapio_detail, name='cardapio'),
    path('reserva/', views.reserva, name='reserva'),
    path('contato/', views.contato, name='contato'),
    path('cancela_reserva/<int:id>', views.cancela_reserva, name='cancela_reserva'),
]
