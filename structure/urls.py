"""Определяет схемы URL для structure"""

from django.urls import path
from django.urls import reverse

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('department/<order_by>/<direction>/', EmployeesView.as_view(), name='department'),
    path('department/<int:position_id>/<order_by>/<direction>/', EmployeesView.as_view(), name='department'),
    # path('department/<int:pk>/', EmployeesView.as_view(), name='department'),
    path('clear-search/', clear_search, name='clear_search'),
    path('employee-detail/<int:pk>/', employee_detail, name='employee_detail'),
    path('update_employee_details/<int:pk>/', update_employee_details, name='update_employee_details'),
    path('delete-employee/<int:pk>/', delete_employee, name='delete_employee'),
    path('add-employee/<filter>/<direction>/', EmployeeCreateView.as_view(), name='add_employee'),
    path('add-employee/', EmployeeCreateView.as_view(), name='add_employee'),
]
