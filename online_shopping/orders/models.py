from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from company.models import CompanyInfo 
import datetime

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    delivery_estimate = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)  

    def __str__(self):
        return f"Order by {self.user.username} for {self.product.name}"
