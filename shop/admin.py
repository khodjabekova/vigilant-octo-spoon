from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'price', 'status']
    search_fields = ['title', 'sku']
    list_filter = ['status']
