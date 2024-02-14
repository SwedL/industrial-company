from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView

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


def employees_list(request, position_id=None, page=1):
    employees = Employee.objects.filter(position=position_id) if position_id else Employee.objects.all()
    per_page = 20
    paginator = Paginator(employees, per_page)
    paginator.get_elided_page_range(number=10, on_each_side=3, on_ends=2)
    employees_paginator = paginator.page(page)

    context = {
        'title': 'Список сотрудников',
        'employees': employees_paginator,
        'position_id': position_id,
        'number': page,
    }

    return render(request, 'structure/employees-list.html', context)


class EmployeesListView(ListView):
    template_name = 'structure/employees-list.html'
    context_object_name = 'employees'
    paginate_by = 20

    def get_queryset(self):
        return Employee.objects.filter(position=self.kwargs['position_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        # context['position_id'] = self.kwargs['position_id']
        return context

