from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),

    path(
        'projetos/novo/',
        views.criar_projeto,
        name='criar_projeto'
    ),

    path(
        'projetos/<int:pk>/editar/',
        views.editar_projeto,
        name='editar_projeto'
    ),

    path(
        'projetos/<int:pk>/excluir/',
        views.excluir_projeto,
        name='excluir_projeto'
    ),
]