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

    name = models.CharField(max_length=120, unique=True, verbose_name="Nome")
    slug = models.SlugField(unique=True, blank=True)

    logo = models.ImageField(upload_to="restaurantes/logos/", blank=True, null=True, verbose_name="Logo")

    description = models.TextField(blank=True, verbose_name="Descrição", help_text="Descrição curta do restaurante")
    cuisine_type = models.CharField(max_length=30, choices=CUISINE_TYPES, default="outros", verbose_name="Tipo de Cozinha")

    latitude = models.FloatField(blank=True, null=True, verbose_name="Latitude")
    longitude = models.FloatField(blank=True, null=True, verbose_name="Longitude")
    building = models.CharField(max_length=80, blank=True, verbose_name="Prédio", help_text="Ex: Frings, Pilotis, etc.")

    opening_hours = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Horário de Funcionamento",
        help_text="Ex: Seg–Sex 8h–22h"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    instagram = models.URLField(blank=True, verbose_name="Instagram")
    website = models.URLField(blank=True, verbose_name="Site")

    price_level = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Nível de Preço",
        help_text="1–5 (quanto mais alto, mais caro)"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        ordering = ["name"]
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name="Nome")
    icon = models.CharField(max_length=80, blank=True, verbose_name="Ícone", help_text="Nome do ícone da sua UI (opcional)")

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="dishes", verbose_name="Restaurante")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")

    name = models.CharField(max_length=120, verbose_name="Nome")
    slug = models.SlugField(blank=True)

    description = models.TextField(blank=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")

    is_vegan = models.BooleanField(default=False, verbose_name="Vegano")
    is_vegetarian = models.BooleanField(default=False, verbose_name="Vegetariano")
    is_gluten_free = models.BooleanField(default=False, verbose_name="Sem Glúten")

    available = models.BooleanField(default=True, verbose_name="Disponível")
    image = models.ImageField(upload_to="pratos/", blank=True, null=True, verbose_name="Imagem")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        ordering = ["name"]
        verbose_name = "Prato"
        verbose_name_plural = "Pratos"

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

