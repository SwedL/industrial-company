from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models.expressions import RawSQL
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, View, CreateView

from structure.forms import UserLoginForm, SearchEmployeeForm
from structure.models import Employee, Position
from .forms import AddEmployeeForm, UpdateEmployeeDetailForm


""" 
Словарь для хранения фильтра sql запроса и данных формы поиска
по полям страницы представления EmployeesView
{'where_for_sql': 'WHERE last_name LIKE '%..%' AND position_id = .. AND ...}, 'form_data': form.clean_data}
"""



class UserLoginView(LoginView):
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
    """Представление отображающее страницу структуры компании в древовидной форме"""

    template_name = 'structure/structure_company.html'
    title = 'Структура компании'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # при открытии страницы стираются фильтры сортировки и поиска представления EmployeesView
        # common_form_data.clear()
        context['staff'] = request.user.has_perm('structure.change_employee')
        context['title'] = self.title
        return self.render_to_response(context)


class EmployeesView(LoginRequiredMixin, View):
    """
    Представление отображающее список сотрудников с использованием фильтров и формы поиска.
    Изначально при переходе на страницу, по блоку отдела, используется:
     фильтр отдела - position,
     сортировка по id сотрудника в прямом порядке
    Поиск позволяет фильтровать сотрудников в форме поиска,
    а также искать по неполному совпадению значений полей.
    """

    paginate_by = 25
    title = 'Список сотрудников'
    common_form_data = {
        'last_name': '',
        'first_name': '',
        'patronymic': '',
        'position_id': '',
        'employment_date': '',
        'salary': '',
    }

    # @classmethod
    # def clear_common_form_data(cls, common_form_data: dict):
    #     t = cls.common_form_data
    #     g = common_form_data
    #     common_form_data.update(cls.common_form_data)
    #     m = 0

    def get_employees_list(self, order_by, direction):
        # меняем сортировку на обратную если условие верно
        if direction == 'descend':
            order_by = '-' + order_by

        last_name = self.common_form_data.get('last_name', '')
        first_name = self.common_form_data.get('first_name', '')
        patronymic = self.common_form_data.get('patronymic', '')

        employees_list = Employee.objects.filter(
            Q(last_name__contains=f'{last_name}') &
            Q(first_name__contains=f'{first_name}') &
            Q(patronymic__contains=f'{patronymic}')
        ).order_by(order_by).annotate(num=RawSQL('row_number() over ()', []))

        # если в форме есть фильтр по отделу, то добавляем его в список фильтров
        if self.common_form_data['position_id']:
            employees_list = employees_list.filter(position_id=self.common_form_data['position_id'])

        if self.common_form_data['salary']:
            employees_list = employees_list.filter(salary=self.common_form_data['salary'])

        if self.common_form_data['employment_date']:
            employees_list = employees_list.filter(employment_date=self.common_form_data['employment_date'])

        return employees_list

    def get(self, request, order_by: str, direction: str, position_id: int = None):

        # если переход впервые - по блоку отдела, то фильтруем по position_id и заносим данные в
        if not request.GET.get('page') and position_id:
            self.common_form_data = {'last_name': '', 'first_name': '', 'patronymic': '', 'position_id': position_id,
                                     'employment_date': '', 'salary': ''}
        if request.GET.get('page') and position_id:
            # получаем данные из формы поиска sql запроса
            form = SearchEmployeeForm(self.common_form_data)

        form = SearchEmployeeForm(self.common_form_data)
        employees_list = self.get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'position_id': position_id,
            'title': self.title,
            'staff': request.user.has_perm('structure.change_employee'),
        }

        return render(request, 'structure/department.html', context=context)

    def post(self, request, order_by: str, direction: str, position_id: int = None):
        # nonlocal common_form_data

        form = SearchEmployeeForm(request.POST)
        # position_id = request.POST.get('position_id')  # отдел берём из request.POST

        if form.is_valid():
            # получаем фильтры для sql запроса из формы и обновляем словарь common_form_data
            self.common_form_data.update(form.cleaned_data)

        # если фильтров поиска не поступало, то словарь common_form_data очищается
        # иначе в словарь заносятся фильтры под ключом where_for_sql и данные формы
        # под ключом request_data
        # if not form.cleaned_data:
        #     common_form_data = dict.fromkeys(form.cleaned_data.keys(), '')

        employees_list = self.get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'position_id': position_id,
            'title': self.title,
            'staff': request.user.has_perm('structure.change_employee'),
        }

        return render(request, 'structure/department.html', context=context)


@login_required
@require_http_methods(['GET'])
def clear_search(request):
    """Функция для очистки полей формы поиска EmployeesView"""
    form = SearchEmployeeForm()
    return render(request, 'structure/search_form.html', context={'form': form})


@login_required
@require_http_methods(['GET'])
def employee_detail(request, pk, num):
    """Функция для возврата исходных данных, при отмене изменений данных сотрудника"""
    employee = get_object_or_404(Employee, pk=pk)
    employee.num = num
    context = {
        'employee': employee,
    }
    return render(request, 'structure/employee_detail.html', context=context)


@permission_required('structure.change_employee')
def update_employee_details(request, pk, num):
    """Функция изменения данных сотрудника"""

    employee = get_object_or_404(Employee, pk=pk)
    # employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateEmployeeDetailForm(request.POST, instance=employee)
        if form.is_valid():
            if any(map(lambda d: d == 'position', form.changed_data)):
                # добавляем вакансию в предыдущей должности, если у сотрудника была должность
                if form.initial['position']:
                    Position.objects.filter(id=form.initial['position']).update(vacancies=F('vacancies') + 1)
                # уменьшаем кол-во вакансий в новой должности сотрудника, если у сотрудника была должность
                if form.data['position']:
                    Position.objects.filter(id=form.data['position']).update(vacancies=F('vacancies') - 1)

            # сохраняем изменённые данные сотрудника
            employee = form.save()
            employee.num = num
            context = {
                'employee': employee,
                'staff': request.user.has_perm('structure.change_employee'),
            }
            return render(request, 'structure/employee_detail.html', context=context)
    else:
        form = UpdateEmployeeDetailForm(instance=employee)
    return render(request, 'structure/partial_employee_update_form.html', {'employee': employee, 'form': form, 'num': num})


@permission_required('structure.change_employee')
@require_http_methods(['DELETE'])
def delete_employee(request, pk):
    """Функция удаления сотрудника из базы данных (кнопка уволить)"""
    employee = get_object_or_404(Employee, pk=pk)
    # при увольнении сотрудника вакансии его должности увеличиваем на 1
    if employee.position:
        employee.position.vacancies += 1
        employee.position.save()
    employee.delete()
    return HttpResponse()


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    form_class = AddEmployeeForm
    permission_required = 'structure.change_employee'
    success_url = reverse_lazy('structure:recruit_distribution')
    template_name = 'structure/recruit_distribution.html'
    title = 'Найм и распределение'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # common_form_data.clear()

        sql = f'SELECT ROW_NUMBER() OVER(ORDER BY last_name) AS num, * FROM structure_employee WHERE position_id is NULL ORDER BY last_name'
        context['employees'] = Employee.objects.raw(sql)
        context['staff'] = self.request.user.has_perm('structure.change_employee')
        context['title'] = self.title

        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')