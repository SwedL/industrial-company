"""Определяет схемы URL для structure"""

from django.urls import path

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('employees-list/<int:position_id>/<int:page>/', employees_list, name='employees_list'),
    # path('employees-list/', employees_list, name='employees_list'),
]
