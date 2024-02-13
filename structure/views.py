from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from structure.forms import UserLoginForm
from structure.models import Position, Employee
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.core.paginator import Paginator


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'structure/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('structure:structure_company')


class StructureCompanyTemplateView(TemplateView):
    template_name = 'structure/structure-company.html'


# class PositionView(View):
#     def get(self, request, position_id):
#         position = Position.objects.filter(id=position_id).first()
#         employee = position.employee_set.all().first()
#         manager_name = f'{employee.last_name} {employee.first_name[0]}.{employee.patronymic[0]}.'
#
#         context = {
#             'position_name': position.name,
#             'manager_name': manager_name,
#         }
#         return render(request, 'structure/employees-list.html', context=context)


def employees_list(request, position_id, page=1):
    employees = Employee.objects.all()
    per_page = 20
    paginator = Paginator(employees, per_page)
    employees_paginator = paginator.page(page)

    context = {
        'title': 'Список сотрудников',
        'employees': employees_paginator,
    }

    return render(request, 'structure/employees-list.html', context)

