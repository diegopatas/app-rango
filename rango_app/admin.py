from django.contrib import admin
from .models import Ingredient, Inventory

admin.site.register(Inventory)
admin.site.register(Ingredient)