from django.contrib import admin
from .models import Product





@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    pass
