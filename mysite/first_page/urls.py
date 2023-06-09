from django.urls import path
from .views import *

urlpatterns = [
    path('', views_first_page, name='Главная страница')
]