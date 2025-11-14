from django.contrib import admin
from django.urls import path
from loja import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial
    path('', views.card_list, name='card_list'),

    # Detalhes da carta
    path('card/<int:card_id>/', views.card_detail_view, name='card_detail'),

    # Carrinho
    path('add-to-cart/<int:card_id>/', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
