from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, View, ListView, CreateView
from django.core.paginator import Paginator

from structure.forms import UserLoginForm, SearchEmployeeForm
from structure.models import Position, Employee
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.core.paginator import Paginator
from django.urls import reverse

from .forms import AddEmployeeForm


common_sql = []


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'structure/login.html'


class StructureCompanyTemplateView(TemplateView):
    template_name = 'structure/structure_company.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        common_sql.clear()
        return self.render_to_response(context)


class EmployeesView(View):
    paginate_by = 25

    def get(self, request, position_id: int, order_by: str, direction: str):
        if common_sql:
            form = SearchEmployeeForm(common_sql[1])
        else:
            form = SearchEmployeeForm()

        if direction == 'descend':
            order_by += ' DESC'

        if common_sql:
            sql = common_sql[0]
        else:
            sql = f'SELECT ROW_NUMBER() OVER(ORDER BY {order_by}) AS num, * FROM structure_employee WHERE position_id = {position_id} ORDER BY {order_by}'

        employees_list = Employee.objects.raw(sql)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'department': position_id,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'form': form,
        }
        return render(request, 'structure/department.html', context=context)

    def post(self, request, position_id: int, order_by: str, direction: str):

        search_key_list = ['last_name', 'first_name', 'patronymic', 'employment_date', 'salary']
        request_dict_from_the_search_key_list = {i: request.POST[i] for i in search_key_list}

        list_filters_for_sql = [f'{k} LIKE "%{v}%"' for k, v in request_dict_from_the_search_key_list.items() if v]
        if not list_filters_for_sql:
            common_sql.clear()

        # TODO replace sql in common_sql on WHERE
        list_filters_for_sql.insert(0, f'WHERE position_id = {position_id}')
        where_for_sql = ' AND '.join(list_filters_for_sql)

        if direction == 'descend':
            order_by += ' DESC'

        sql = f'SELECT ROW_NUMBER() OVER(ORDER BY {order_by}) AS num, * FROM structure_employee {where_for_sql} ORDER BY {order_by}'
        common_sql.insert(0, sql)
        common_sql.insert(1, request.POST)

        employees_list = Employee.objects.raw(sql)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if common_sql:
            form = SearchEmployeeForm(common_sql[1])
        else:
            form = SearchEmployeeForm()

        context = {
            'employees': page_obj,
            'department': position_id,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'form': form,
        }
        return render(request, 'structure/department.html', context=context)


class EmployeeCreateView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'structure/add_employee.html'
    success_url = reverse_lazy('structure:add_employee')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        position_id = None
        filter = None

        if self.kwargs:
            filter = self.kwargs['filter']
            direction = self.kwargs['direction']

        if filter:
            if filter == "id":
                if direction == 'ascend':
                    employees_list = Employee.objects.filter(position=position_id).order_by('pk')
                else:
                    employees_list = Employee.objects.filter(position=position_id).order_by('-pk')
            else:
                if direction == 'ascend':
                    employees_list = Employee.objects.filter(position=position_id).order_by(filter)
                else:
                    employees_list = Employee.objects.filter(position=position_id).order_by('-' + filter)

        else:
            employees_list = Employee.objects.filter(position=position_id)

        context['employees'] = employees_list
        context['department'] = 0

        return context


@require_http_methods(['DELETE'])
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return HttpResponse()


@require_http_methods(['GET'])
def employees_list_sort(request, position_id, filter, direction):
    paginate_by = 20
    if position_id == 0:
        position_id = None

    if filter == "id":
        if direction == 'ascend':
            employees_list = Employee.objects.filter(position=position_id).order_by('pk')
        else:
            employees_list = Employee.objects.filter(position=position_id).order_by('-pk')
    else:
        if direction == 'ascend':
            employees_list = Employee.objects.filter(position=position_id).order_by(filter)
        else:
            employees_list = Employee.objects.filter(position=position_id).order_by('-' + filter)

    paginator = Paginator(employees_list, paginate_by)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'employees': page_obj,
        'paginator_range': page_obj.paginator.get_elided_page_range(page_number),
        'filter': filter,
        'direction': direction,
    }
    return render(request, 'structure/employees_list.html', context=context)
