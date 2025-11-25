from django import forms
from .models import *

class RestaurantesForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = []