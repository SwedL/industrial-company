"""Определяет схемы URL для structure"""

from django.urls import path

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('employees-list/<int:position_id>/', employees_list, name='position_view'),
]
