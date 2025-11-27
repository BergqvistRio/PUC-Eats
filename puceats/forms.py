from django import forms
from django.forms import inlineformset_factory

from .models import Restaurant, Dish, Category


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "logo",
            "description",
            "cuisine_type",
            "latitude",
            "longitude",
            "building",
            "opening_hours",
            "phone",
            "instagram",
            "website",
            "price_level",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "opening_hours": forms.TextInput(attrs={"placeholder": "Ex: Seg–Sex 8h–22h"}),
        }


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "category",
            "description",
            "price",
            "is_vegan",
            "is_vegetarian",
            "is_gluten_free",
            "available",
            "image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "icon"]


DishFormSet = inlineformset_factory(
    parent_model=Restaurant,
    model=Dish,
    form=DishForm,
    extra=1,            
    can_delete=True,    
    
)
