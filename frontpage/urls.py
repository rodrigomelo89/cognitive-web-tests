from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='posts'),
    path('formulario/', views.formulario, name='formulario'),
    path('teste_cognitivo/<int:pk>/', views.teste_cognitivo, name='teste_cognitivo'),
    path('teste_cognitivo/resultados/<int:pk>/', views.respostas, name='respostas'),
]
