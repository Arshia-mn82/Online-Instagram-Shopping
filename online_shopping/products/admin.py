from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)
    list_filter = ('price',)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
