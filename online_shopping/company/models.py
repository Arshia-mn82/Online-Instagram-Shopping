from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"Company Info: {self.address}, {self.telephone}"
