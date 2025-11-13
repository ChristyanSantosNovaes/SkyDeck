from django.urls import path
from . import views # Importa as views do próprio app 'loja'

# loja/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list_view, name='card_list'),
    path('card/<int:card_id>/', views.card_detail_view, name='card_detail'),
    path('add_to_cart/<int:card_id>/', views.add_to_cart, name='add_to_cart'),
]