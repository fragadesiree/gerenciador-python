from django.urls import path
from .views.tarefas_views import *
from .views.usuarios_views import *

urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefas/', cadastrar_tarefas, name='cadastrar_tarefas'),
    path('editar_tarefas/<int:id>', editar_tarefas, name='editar_tarefas'),
    path('remover_tarefas/<int:id>', remover_tarefas, name='remover_tarefas'),
    path('cadastrar_usuarios/', cadastrar_usuarios, name='cadastrar_usuarios'),
    path('logar_usuarios/', logar_usuarios, name='logar_usuarios'),
    path('deslogar_usuarios/', deslogar_usuarios, name='deslogar_usuarios'),
]