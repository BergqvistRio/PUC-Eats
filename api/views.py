from django.shortcuts import render
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
