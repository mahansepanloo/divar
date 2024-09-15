from django.contrib import admin
from .models import Product,Category






@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class Admin(admin.ModelAdmin):
    pass
