from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('cadastro_item/', views.cadastro_item_view, name='cadastro_item'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('cadastro_anuncio/', views.cadastro_anuncio_view, name='cadastro_anuncio'),
    path('anunciados/', views.anunciados_view, name='anunciados'),
]

