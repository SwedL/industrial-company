from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, View, ListView, CreateView

from structure.forms import UserLoginForm
from structure.models import Position, Employee
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.core.paginator import Paginator
from django.urls import reverse

from .forms import AddEmployeeForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'structure/login.html'


class StructureCompanyTemplateView(TemplateView):
    template_name = 'structure/structure_company.html'


class EmployeesListView(ListView):
    template_name = 'structure/department.html'
    context_object_name = 'employees'
    paginate_by = 20

    def get_queryset(self):
        return Employee.objects.filter(position=self.kwargs['position_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        return context


class EmployeeCreateView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'structure/add_employee.html'
    success_url = reverse_lazy('structure:add_employee')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(position=None)
        return context


@require_http_methods(['DELETE'])
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return HttpResponse()


@require_http_methods(['GET'])
def employees_list_sort(request, filter, direction):
    print('sfdsfsf')
    if filter == "id":
        if direction == 'ascend':
            employees_list = Employee.objects.filter(position=None).order_by('pk')
        else:
            employees_list = Employee.objects.filter(position=None).order_by('-pk')
    else:
        if direction == 'ascend':
            employees_list = Employee.objects.filter(position=None).order_by(filter)
        else:
            employees_list = Employee.objects.filter(position=None).order_by('-' + filter)
    return render(request, 'structure/employees_list.html', {'employees': employees_list})
