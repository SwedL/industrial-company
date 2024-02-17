"""Определяет схемы URL для structure"""

from django.urls import path
from django.urls import reverse

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('employees-list/<int:position_id>/', EmployeesListView.as_view(), name='employees_list'),
    path('add-employee/', AddEmployee.as_view(), name='add_employee'),
    path('create-employee/', AddEmployee.as_view(), name='create_employee'),
    # path('employees-list/<int:position_id>/<int:page>/', employees_list, name='employees_list'),
]
