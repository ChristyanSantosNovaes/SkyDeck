from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Game, Order, OrderItem, CardSet


def card_list(request):
    cards = Card.objects.all()

    search = request.GET.get('search')
    if search:
        cards = cards.filter(name__icontains=search)

    code = request.GET.get('code')
    if code:
        cards = cards.filter(card_id__icontains=code)

    color = request.GET.get('color')
    if color and color != "":
        cards = cards.filter(color=color)

    set_id = request.GET.get('set')
    if set_id and set_id != "":
        cards = cards.filter(card_set__id=set_id)

    order = request.GET.get('order')
    if order == "asc":
        cards = cards.order_by("price")
    elif order == "desc":
        cards = cards.order_by("-price")

    colors = Card.objects.values_list("color", flat=True).distinct()
    sets = CardSet.objects.all()

    return render(request, "loja/card_list.html", {
        "cards": cards,
        "colors": colors,
        "sets": sets,
        "titulo_pagina": "Catálogo de Cartas",
    })


def card_detail_view(request, card_id):
    card = get_object_or_404(Card, id=card_id)

    return render(request, "loja/card_detail.html", {
        "card": card,
        "titulo_pagina": card.name,
    })


def add_to_cart(request, card_id):
    card = get_object_or_404(Card, id=card_id)

    order, created = Order.objects.get_or_create(
        user=request.user,
        completed=False
    )

    item, item_created = OrderItem.objects.get_or_create(
        order=order,
        card=card
    )

    if not item_created:
        item.quantity += 1
        item.save()

    return redirect('card_detail', card_id=card.id)
