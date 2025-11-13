from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Game, Order, OrderItem


# 📦 Vitrine de Cards (com filtros)
def card_list_view(request):
    cards = Card.objects.all()
    games = Game.objects.all()

    # 🔹 Filtro por jogo
    game_id = request.GET.get('game')
    if game_id:
        cards = cards.filter(card_set__game__id=game_id)

    # 🔹 Filtro por cor
    color = request.GET.get('color')
    if color:
        cards = cards.filter(color=color)

    # 🔹 Filtro por nome (busca)
    search = request.GET.get('search')
    if search:
        cards = cards.filter(name__icontains=search)

    # 🔹 Ordenação por preço
    order = request.GET.get('order')
    if order == 'asc':
        cards = cards.order_by('price')
    elif order == 'desc':
        cards = cards.order_by('-price')

    context = {
        'cards': cards,
        'games': games,
        'titulo_pagina': 'Catálogo de Cartas',
    }
    return render(request, 'loja/card_list.html', context)


# 📄 Detalhes da Carta
def card_detail_view(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    
    context = {
        'titulo_pagina': card.name,
        'card': card,
    }
    
    return render(request, 'loja/card_detail.html', context)


# 🛒 Adicionar ao carrinho
def add_to_cart(request, card_id):
    card = get_object_or_404(Card, id=card_id)

    # Pega (ou cria) um pedido ativo
    order, created = Order.objects.get_or_create(
        user=request.user if request.user.is_authenticated else None,
        complete=False
    )

    # Verifica se o card já está no pedido
    order_item, created = OrderItem.objects.get_or_create(order=order, card=card)
    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('card_detail', card_id=card.id)
