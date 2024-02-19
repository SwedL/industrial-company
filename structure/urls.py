"""Определяет схемы URL для structure"""

from django.urls import path
from django.urls import reverse

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('department/<int:position_id>/<order_by>/<direction>/', EmployeesView.as_view(), name='department'),
    path('add-employee/<filter>/<direction>/', EmployeeCreateView.as_view(), name='add_employee'),
    path('add-employee/', EmployeeCreateView.as_view(), name='add_employee'),
    # path('create-employee/', AddEmployee.as_view(), name='create_employee'),
    path('delete-employee/<int:pk>/', delete_employee, name='delete_employee'),
    path("employees_list_sort/<filter>/<direction>/<int:position_id>/", employees_list_sort, name="employees_list_sort"),
    # path('employees-list/<int:position_id>/<int:page>/', employees_list, name='employees_list'),
]
