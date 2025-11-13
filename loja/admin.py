from django.contrib import admin
# 1. Importamos nossos modelos
from .models import Game, CardSet, Card
# 2. Registramos o modelo Game
admin.site.register(Game)

# 3. Registramos o modelo CardSet
admin.site.register(CardSet)

# 4. Registramos o modelo Card
# Opcionalmente, podemos criar uma classe Admin para controlar como a tabela aparece:
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista principal (Ex: Nome, Preço, Estoque)
    list_display = ('name', 'card_id', 'rarity', 'price', 'stock', 'card_set')

    search_fields = ('name', 'card_id')

    list_filter = ('rarity', 'card_set')