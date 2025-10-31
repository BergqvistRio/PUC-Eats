from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'puceats/index.html')

def exemplo_consumir_api(request):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        return JsonResponse({'success': True, 'data': data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

