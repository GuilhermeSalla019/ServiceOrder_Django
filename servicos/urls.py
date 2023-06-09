from django.urls import path
from . import views

"""URL Redireciona para serviços """

urlpatterns = [
    path('novo_servico/', views.novo_servico, name="novo_servico"),
    path('listar_servico/', views.listar_servico, name="listar_servico"),
    path('servico/<str:identificador>/', views.servico, name="servico"),
    path('gerar_os/<str:identificador>/', views.gerar_os, name="gerar_os"),
    path('finalizar_servico/<str:identificador>/', views.finalizar_servico, name='finalizar_servico'),
    path('servico/editar/<str:identificador>/', views.editar_servico, name='editar_servico'),
]
