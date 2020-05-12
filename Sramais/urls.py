from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Sramais-inicio'),
    path('guia/', views.guia, name='Sramais-sobre'),
    path('adicionar/', views.adicionar, name='Sramais-adicionar'),
    path('editar-perfil/<int:id>', views.editar_perfil, name='Sramais-editar-perfil'),
    path('delete/<int:id>', views.delete, name="Sramais-delete"),
    path('invalido/', views.nao_encontrado, name = 'Sramais-invalido'),
    path('cadastro/', views.unidade, name='Sramais-cadastro'),
    path('unidade/<str:nome>', views.apresentacao, name='Sramais-unidade'),
    path('registro/', views.registro, name='Sramais-registro'),
    path('editar-usuario/<int:id>', views.editar_usuario, name='Sramais-editar-usuario'),
    path('editar-unidade/<int:id>', views.editar_unidade, name='Sramais-editar-unidade')

]