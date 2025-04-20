from collections import defaultdict

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import F, Q, QuerySet
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, TemplateView, View

from structure.forms import (AddEmployeeForm, SearchEmployeeForm,
                             UpdateEmployeeDetailForm, UserLoginForm)
from structure.models import Employee, Position
from structure.permissions.staff_permissions import staff_permission

# Словарь для хранения данных полей фильтра SearchEmployeeForm
common_form_data = defaultdict(str)


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
        context['staff'] = request.user.has_perm('structure.change_employee')
        context['title'] = self.title
        return self.render_to_response(context)


def get_employees_list(order_by: str, direction: str) -> QuerySet:
    """ Функция фильтрует Employee QuerySet согласно заполненным полям формы SearchEmployeeForm,
        возвращает пронумерованный и отсортированный queryset """

    # если условие верно сортировка меняется на обратную
    if direction == 'descend':
        order_by = '-' + order_by

    employees_list = Employee.objects.filter(
        Q(last_name__contains=f'{common_form_data["last_name"]}') &
        Q(first_name__contains=f'{common_form_data["first_name"]}') &
        Q(patronymic__contains=f'{common_form_data["patronymic"]}')
    ).select_related('position')

    # дополнительная фильтрация, если в форме есть фильтр по отделу, дате трудоустройства или зарплате
    if common_form_data['position_id']:
        employees_list = employees_list.filter(position_id=common_form_data['position_id'])
    elif common_form_data['employment_date']:
        employees_list = employees_list.filter(employment_date=common_form_data['employment_date'])
    elif common_form_data['salary']:
        employees_list = employees_list.filter(salary=common_form_data['salary'])

    return employees_list.order_by(order_by).annotate(num=Window(expression=RowNumber(), order_by=[order_by]))


class EmployeesView(LoginRequiredMixin, View):
    """
    Представление страницы списка сотрудников с использованием фильтров формы поиска,
     сортировки данных и изменения данных сотрудника
    Поиск позволяет фильтровать сотрудников в форме поиска:
        по полному и неполному совпадению значений полей - фамилия, имя, отчество
        по полному совпадению значений полей - дата приёма на работу, зарплата
    """

    paginate_by = 25
    title = 'Список сотрудников'

    def get(self, request, order_by: str, direction: str, position_id: str = None):
        global common_form_data

        # если переход впервые - по блоку отдела, то фильтрация по position_id и занесение фильтра в common_form_data
        if not request.GET.get('page') and position_id:
            common_form_data.clear()
            common_form_data['position_id'] = position_id

        form = SearchEmployeeForm(common_form_data)

        employees_list = get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': common_form_data,
            'title': self.title,
            'staff': request.user.has_perm('structure.change_employee'),
        }

        return render(request, 'structure/department.html', context=context)

    def post(self, request, order_by: str, direction: str, position_id: str = None):

        form = SearchEmployeeForm(request.POST)

        # обновление словаря common_form_data
        if form.is_valid():
            common_form_data.update(form.cleaned_data)

        employees_list = get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': common_form_data,
            'title': self.title,
            'staff': request.user.has_perm('structure.change_employee'),
        }

        return render(request, 'structure/department.html', context=context)


@login_required
@require_http_methods(['GET'])
def clear_search(request):
    """ Функция для очистки полей формы поиска EmployeesView """

    form = SearchEmployeeForm()
    return render(request, 'structure/search_form.html', context={'form': form})


@login_required
@require_http_methods(['GET'])
def employee_detail(request, pk, num):
    """ Функция для возврата исходных данных, при отмене изменений данных сотрудника """

    employee = get_object_or_404(Employee, pk=pk)
    employee.num = num
    context = {
        'employee': employee,
        'staff': request.user.has_perm('structure.change_employee'),
    }
    return render(request, 'structure/employee_detail.html', context=context)


@permission_required(staff_permission)
def update_employee_details(request, employee_id, employee_num):
    """ Функция изменения данных сотрудника """

    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = UpdateEmployeeDetailForm(request.POST, instance=employee)
        if form.is_valid():
            if any(map(lambda d: d == 'position', form.changed_data)):
                # добавление вакансии в предыдущей должности, если у сотрудника была должность (не None)
                if form.initial['position']:
                    Position.objects.filter(id=form.initial['position']).update(vacancies=F('vacancies') + 1)
                # уменьшение кол-ва вакансий в новой должности сотрудника, если у сотрудника была должность (не None)
                if form.data['position']:
                    Position.objects.filter(id=form.data['position']).update(vacancies=F('vacancies') - 1)

            # сохранение изменённых данных сотрудника
            employee = form.save()
            employee.num = employee_num
            context = {
                'employee': employee,
                'staff': request.user.has_perm('structure.change_employee'),
            }
            return render(request, 'structure/employee_detail.html', context=context)

    context = {
        'employee': employee,
        'form': UpdateEmployeeDetailForm(instance=employee),
        'employee_num': employee_num,
    }

    return render(request, 'structure/partial_employee_update_form.html', context=context)


@permission_required(staff_permission)
@require_http_methods(['DELETE'])
def delete_employee(request, pk):
    """ Функция удаления сотрудника из базы данных (кнопка уволить) """

    employee = get_object_or_404(Employee, pk=pk)
    # при увольнении сотрудника вакансии его должности увеличивается на 1
    if employee.position:
        employee.position.vacancies += 1
        employee.position.save()
    employee.delete()

    return HttpResponse()


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    """ Представление страницы добавления новых сотрудников в компанию
    и распределение по должностям незанятых сотрудников """

    form_class = AddEmployeeForm
    permission_required = 'structure.change_employee'
    success_url = reverse_lazy('structure:recruit_distribution')
    template_name = 'structure/recruit_distribution.html'
    title = 'Найм и распределение'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        employees_list = Employee.objects.filter(
            position=None
        ).order_by(
            'employment_date'
        ).annotate(
            num=Window(expression=RowNumber(), order_by=['employment_date'])
        )

        context['employees'] = employees_list
        context['staff'] = self.request.user.has_perm('structure.change_employee')
        context['title'] = self.title

        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
