from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cognitive_webapp'

# página a ser exibida, função vinculada a página e o nome pra ser usado como id pros returns das funções no view
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('formulario/', views.formulario, name='formulario'),
    path('teste_cognitivo/<int:pk>/', views.teste_cognitivo, name='teste'),
    path('teste_cognitivo/resultados/<int:pk>/', views.respostas, name='respostas'),
]


