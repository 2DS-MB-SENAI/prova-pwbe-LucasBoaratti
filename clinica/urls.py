from django.urls import path
from . import views

urlpatterns = [
    path("medicos/", view=views.listar_medicos, name="Listar todos os médicos."),
    path("consultas/nova/", view=views.criar_consulta, name="Criar uma consulta."),
    path("consultas/<int:pk>/", view=views.detalhes_consulta, name="Detalhes da consulta."),
]