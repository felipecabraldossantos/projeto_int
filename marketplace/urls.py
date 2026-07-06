from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_item/', views.cadastro_item_view, name='cadastro_item'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('cadastro_anuncio/', views.cadastro_anuncio_view, name='cadastro_anuncio'),
    path('anunciados/', views.anunciados_view, name='anunciados'),
    path('anuncio/<int:id>/', views.anuncio_view,name='anuncio'),
    path('anuncio/editar/<int:id>/', views.editar_anuncio_view, name='editar_anuncio'),
    path('anuncio/vender/<int:id>/', views.vender_anuncio, name='vender_anuncio'),
]
