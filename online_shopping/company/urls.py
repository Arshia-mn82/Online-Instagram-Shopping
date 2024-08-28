from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.get_company_info, name='get_company_info'),
]
