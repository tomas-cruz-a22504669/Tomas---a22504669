from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos_view, name='projetos'),
    path('novo/', views.novo_projeto_view, name='novo_projeto'),
    path('edita/<int:projeto_id>/', views.edita_projeto_view, name='edita_projeto'),
    path('apaga/<int:projeto_id>/', views.apaga_projeto_view, name='apaga_projeto'),
]