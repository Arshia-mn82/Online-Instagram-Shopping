from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('pay/<int:order_id>/', views.mark_as_paid, name='mark_as_paid'),
    path('order-details/<int:order_id>/', views.order_details, name='order_details'),
]
