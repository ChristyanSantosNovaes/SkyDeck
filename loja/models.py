from django.db import models
from django.contrib.auth.models import User

# Etapa 1.1: O Modelo para o Jogo
class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Etapa 1.2: O Modelo para o Set (Expansão)
class CardSet(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game.name} - {self.name}'


# Etapa 1.3: O Modelo para o Card (O Produto)
class Card(models.Model):
    COLOR_CHOICES = [
        ('red', 'Vermelho'),
        ('blue', 'Azul'),
        ('green', 'Verde'),
        ('purple', 'Roxo'),
        ('black', 'Preto'),
        ('yellow', 'Amarelo'),
        ('multicolor', 'Multicolorido'),
    ]

    TYPE_CHOICES = [
        ('leader', 'Líder'),
        ('character', 'Personagem'),
        ('event', 'Evento'),
        ('stage', 'Estágio'),
        ('navy', 'Navy/SWORD'),
    ]

    card_set = models.ForeignKey('CardSet', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    card_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    rarity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    counter = models.CharField(max_length=20, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    block_icon = models.IntegerField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'[{self.card_id}] {self.name}'




# Etapa 2.1: O Modelo para o Pedido (Order)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'Pedido {self.id}'


# Etapa 2.2: O Item Individual do Pedido (OrderItem)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.card.price * self.quantity

    def __str__(self):
        return f'{self.quantity}x {self.card.name} em Pedido {self.order.id}'
