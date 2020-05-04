from django.urls import path
from . import views


urlpatterns = [
    path('', views.exams_list, name='exams_list')
]