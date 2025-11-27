from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, DishFormSet
from .models import Restaurant
from django.http import JsonResponse
import requests

# Create your views here.

def index(request):
    """
    Página inicial da aplicação
    """
    return render(request, 'api/index.html')

def exemplo_consumir_api(request):
    """
    Exemplo de como consumir uma API externa
    """
    try:
        # Exemplo: consumindo uma API pública
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        return JsonResponse({'success': True, 'data': data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    

def create_restaurant_with_menu(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        formset = DishFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            restaurant = form.save()
            dishes = formset.save(commit=False)

            for dish in dishes:
                dish.restaurant = restaurant
                dish.save()

            # se quiser, redireciona para a página de detalhes
            return redirect("restaurant_detail", slug=restaurant.slug)
    else:
        form = RestaurantForm()
        formset = DishFormSet()

    return render(
        request,
        "restaurants/restaurant_form.html",
        {"form": form, "formset": formset},
    )