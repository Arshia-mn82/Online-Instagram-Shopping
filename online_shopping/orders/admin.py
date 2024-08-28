from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'ordered_at', 'paid', 'delivery_estimate', 'company')
    search_fields = ('user__username', 'product__name')
    list_filter = ('paid', 'ordered_at')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
