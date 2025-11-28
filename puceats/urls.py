from django.urls import path
from . import views

app_name = 'puceats'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('esqueci-senha/', views.esqueci_senha, name='esqueci-senha'),
    path('favoritos/', views.favoritos, name='favoritos'),
    
    # CRUD Pratos
    path('crud/', views.crud, name='crud'),
    path('crud/dish/add/', views.dish_add, name='dish-add'),
    path('crud/dish/<int:dish_id>/edit/', views.dish_edit, name='dish-edit'),
    path('crud/dish/<int:dish_id>/delete/', views.dish_delete, name='dish-delete'),
    
    # CRUD Restaurantes
    path('crud/restaurantes/', views.crud_restaurantes, name='crud-restaurantes'),
    path('crud/restaurant/add/', views.restaurant_add, name='restaurant-add'),
    path('crud/restaurant/<int:restaurant_id>/edit/', views.restaurant_edit, name='restaurant-edit'),
    path('crud/restaurant/<int:restaurant_id>/delete/', views.restaurant_delete, name='restaurant-delete'),
    
    path('exemplo-api/', views.exemplo_consumir_api, name='exemplo-api'),
    path("restaurantes/<slug:slug>/", views.restaurant_detail, name="restaurant_detail"),
]
