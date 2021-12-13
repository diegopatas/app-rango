from django.contrib import admin
from . models import Inventory, Ingredient

admin.site.register(Inventory)
admin.site.register(Ingredient)