from django.contrib import admin
from .models import Restaurant, Category, Dish


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine_type', 'building', 'price_level', 'created_at']
    list_filter = ['cuisine_type', 'price_level']
    search_fields = ['name', 'description', 'building']
    prepopulated_fields = {'slug': ('name',)}
    verbose_name = 'Restaurante'
    verbose_name_plural = 'Restaurantes'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'category', 'price', 'available', 'is_vegan', 'is_vegetarian']
    list_filter = ['restaurant', 'category', 'available', 'is_vegan', 'is_vegetarian', 'is_gluten_free']
    search_fields = ['name', 'description', 'restaurant__name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['available']
    verbose_name = 'Prato'
    verbose_name_plural = 'Pratos'
