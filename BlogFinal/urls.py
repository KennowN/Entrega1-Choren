from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Inicio'),
    path('carniceria/', views.mostrar_carniceria, name='carniceria'),
    path('verduleria/', views.mostrar_verduleria, name='verduleria'),
    path('panaderia/', views.mostrar_panaderia, name='panaderia'),
    path('comercios/', views.mostrar_comercio, name='comercio'),
    path('crear_carniceria/', views.crear_carniceria, name='Agregar carniceria'),
    path('crear_verduleria/', views.crear_verduleria, name='Agregar verduleria'),
    path('crear_panaderia/', views.crear_panaderia, name='Agregar panaderia'),
    path('buscar_carniceria/', views.buscar_carniceria, name='Buscar carniceria'),
    path('buscar_verduleria/', views.buscar_verduleria, name='Buscar verduleria'),
    path('buscar_panaderia/', views.buscar_panaderia, name='Buscar panaderia'),
]
