from django.contrib import admin
from .models import CompanyInfo

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telephone')
    search_fields = ('name',)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"
