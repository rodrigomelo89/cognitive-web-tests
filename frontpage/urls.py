from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='posts'),
    # path('profissional/', views.teste_acompanhado, name='teste_acompanhado'),
    # path('auto_teste/', views.auto_teste, name='auto_teste'),
    path('formulario/<int:pk>/', views.formulario, name='formulario'),
    path('teste_cognitivo/<int:pk>/', views.teste_cognitivo, name='teste_cognitivo'),
    path('teste_cognitivo/resultados/<int:pk>/', views.respostas, name='resultados'),
]
