from django.urls import path
from . import views

app_name = 'puceats'

urlpatterns = [
    path('', views.index, name='index'),
    path('exemplo-api/', views.exemplo_consumir_api, name='exemplo-api'),
]
