from collections import defaultdict

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.core.handlers.asgi import ASGIRequest
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, TemplateView, View

from structure.forms import (AddEmployeeForm, SearchEmployeeForm,
                             UpdateEmployeeDetailForm, UserLoginForm)
from structure.models import Employee
from structure.permissions.staff_permissions import staff_required
from structure.services import update_employee_details_service
from structure.services.employees_view_service import EmployeesViewService


class UserLoginView(LoginView):
    """ Представление домашней страницы для авторизации пользователя """

    form_class = UserLoginForm
    template_name = 'structure/login.html'
    title = 'Авторизация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


def logout_user(request):
    logout(request)
    return redirect('/')


class StructureCompanyTemplateView(LoginRequiredMixin, TemplateView):
    """ Представление страницы структуры компании в древовидной форме """

    template_name = 'structure/structure_company.html'
    title = 'Структура компании'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['staff'] = staff_required(request.user)
        context['title'] = self.title
        return self.render_to_response(context)


class EmployeesView(LoginRequiredMixin, View, EmployeesViewService):
    """
    Представление страницы списка сотрудников с использованием фильтров формы поиска,
     сортировки данных и изменения данных сотрудника
    Поиск позволяет фильтровать сотрудников в форме поиска:
        по полному и неполному совпадению значений полей - фамилия, имя, отчество
        по полному совпадению значений полей - дата приёма на работу, зарплата
    """

    paginate_by = 25
    title = 'Список сотрудников'
    common_form_data = defaultdict(str)

    def get(self, request: ASGIRequest, order_by: str, direction: str, position_id: str = None) -> render:
        context = self.get_context_for_get_request(
            request=request,
            order_by=order_by,
            direction=direction,
            position_id=position_id,
        )
        return render(request, 'structure/department.html', context=context)

    def post(self, request: ASGIRequest, order_by: str, direction: str, position_id: str = None) -> render:
        context = self.get_context_for_post_request(request=request, order_by=order_by, direction=direction)
        return render(request, 'structure/department.html', context=context)


@login_required
@require_http_methods(['GET'])
def clear_search(request: ASGIRequest) -> render:
    """ Функция для очистки полей формы поиска EmployeesView """

    form = SearchEmployeeForm()
    return render(request, 'structure/search_form.html', context={'form': form})


@login_required
@require_http_methods(['GET'])
def employee_detail(request: ASGIRequest, pk: int, num: int) -> render:
    """ Функция для возврата исходных данных, при отмене изменений данных сотрудника """

    employee = get_object_or_404(Employee, pk=pk)
    employee.num = num
    context = {
        'employee': employee,
        'staff': staff_required(request.user),
    }
    return render(request, 'structure/employee_detail.html', context=context)


@user_passes_test(staff_required, login_url='/')
def update_employee_details(request: ASGIRequest, employee_id: int, employee_num: int) -> render:
    """ Функция изменения данных сотрудника """

    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        context = update_employee_details_service.get_context(request=request, employee=employee)
        if context:
            employee.num = employee_num
            return render(request, 'structure/employee_detail.html', context=context)

    context = {
        'employee': employee,
        'form': UpdateEmployeeDetailForm(instance=employee),
        'employee_num': employee_num,
    }

    return render(request, 'structure/partial_employee_update_form.html', context=context)


@user_passes_test(staff_required, login_url='/')
@require_http_methods(['DELETE'])
def delete_employee(request: ASGIRequest, pk: int) -> HttpResponse:
    """ Функция удаления сотрудника из базы данных (кнопка уволить) """

    employee = get_object_or_404(Employee, pk=pk)
    # при увольнении сотрудника вакансии его должности увеличивается на 1
    if employee.position:
        employee.position.vacancies += 1
        employee.position.save()
    employee.delete()

    return HttpResponse()


class EmployeeCreateView(UserPassesTestMixin, CreateView):
    """ Представление страницы добавления новых сотрудников в компанию
    и распределение по должностям незанятых сотрудников """

    form_class = AddEmployeeForm
    success_url = reverse_lazy('structure:recruit_distribution')
    template_name = 'structure/recruit_distribution.html'
    title = 'Найм и распределение'

    def test_func(self):
        return staff_required(self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        employees_list = Employee.objects.filter(
            position=None
        ).order_by(
            'employment_date'
        ).annotate(
            num=Window(expression=RowNumber(), order_by=['employment_date'])
        )

        context['employees'] = employees_list
        context['staff'] = self.test_func()
        context['title'] = self.title

        return context


def pageNotFound(request: ASGIRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
