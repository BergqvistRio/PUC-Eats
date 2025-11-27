from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import Restaurant

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def esqueci_senha(request):
    return render(request, 'EsqueciMinhaSenha.html')

def favoritos(request):
    return render(request, 'Favoritos.html')

def crud(request):
    return render(request, 'crud.html')

def exemplo_consumir_api(request):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        return JsonResponse({'success': True, 'data': data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def restaurant_detail(request, slug):
    """
    Página de detalhes de um restaurante.
    Busca pelo slug e mostra o cardápio.
    """
    restaurant = get_object_or_404(Restaurant, slug=slug)
    dishes = restaurant.dishes.all().select_related("category")

    return render(
        request,
        "restaurants/restaurant_detail.html",
        {
            "restaurant": restaurant,
            "dishes": dishes,
        },
    )