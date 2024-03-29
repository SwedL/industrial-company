""" Схемы URL для structure """

from django.urls import path

from .views import (EmployeeCreateView, EmployeesView,
                    StructureCompanyTemplateView, UserLoginView, clear_search,
                    delete_employee, employee_detail, logout_user,
                    update_employee_details)

app_name = 'structure'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('structure-company/', StructureCompanyTemplateView.as_view(), name='structure_company'),
    path('department/<order_by>/<direction>/', EmployeesView.as_view(), name='department'),
    path('department/<position_id>/<order_by>/<direction>/', EmployeesView.as_view(), name='department'),
    path('clear-search/', clear_search, name='clear_search'),
    path('employee-detail/<int:pk>/<int:num>/', employee_detail, name='employee_detail'),
    path(
        'update_employee_detail/<int:employee_id>/<int:employee_num>',
        update_employee_details,
        name='update_employee_detail',
    ),
    path('delete-employee/<int:pk>/', delete_employee, name='delete_employee'),
    path('recruit_distribution/', EmployeeCreateView.as_view(), name='recruit_distribution'),
]
