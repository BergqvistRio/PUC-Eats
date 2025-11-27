from django.db import models
from django.utils.text import slugify


class Restaurant(models.Model):
    CUISINE_TYPES = [
        ("brasileira", "Brasileira"),
        ("japonesa", "Japonesa"),
        ("italiana", "Italiana"),
        ("árabe", "Árabe"),
        ("vegana", "Vegana"),
        ("cafeteria", "Cafeteria"),
        ("lanches", "Lanches"),
        ("internacional", "Internacional"),
        ("outros", "Outros"),
    ]

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    logo = models.ImageField(upload_to="restaurantes/logos/", blank=True, null=True)

    description = models.TextField(blank=True, help_text="Descrição curta do restaurante")
    cuisine_type = models.CharField(max_length=30, choices=CUISINE_TYPES, default="outros")

    # Localização no campus
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    building = models.CharField(max_length=80, blank=True, help_text="Ex: Frings, Pilotis, etc.")

    # Informações de operação
    opening_hours = models.CharField(
        max_length=120,
        blank=True,
        help_text="Ex: Seg–Sex 8h–22h"
    )
    phone = models.CharField(max_length=20, blank=True)
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)

    # Faixa de preço média (boa prática para apps de cardápio)
    price_level = models.PositiveSmallIntegerField(
        default=1,
        help_text="1–5 (quanto mais alto, mais caro)"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    """
    Categoria de pratos (churrasco, japonês, massas, smoothies, etc).
    Útil para organizar o cardápio dentro de cada restaurante.
    """
    name = models.CharField(max_length=60, unique=True)
    icon = models.CharField(max_length=80, blank=True, help_text="Nome do ícone da sua UI (opcional)")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="dishes")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)

    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="pratos/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

