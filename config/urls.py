from django.contrib import admin
from django.urls import path
from loja import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial: lista de cartas
    path('', views.card_list_view, name='card_list'),

    # Página de detalhes da carta
    path('card/<int:card_id>/', views.card_detail_view, name='card_detail'),

    # Adicionar carta ao carrinho
    path('add-to-cart/<int:card_id>/', views.add_to_cart, name='add_to_cart'),
]

# Exibe imagens durante o modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
