from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, View, CreateView

from structure.forms import UserLoginForm, SearchEmployeeForm
from structure.models import Employee
from .forms import AddEmployeeForm, UpdateEmployeeDetailForm

# словарь для хранения фильтров cql запросов и данных формы поиска
# по полям страницы представления EmployeesView
# {'where_for_sql': {'last_name': '', 'first_name': '', ...}, 'request_data': request.POST}
common_where_and_request_data = {}


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'structure/login.html'


class StructureCompanyTemplateView(TemplateView):
    """Представление отображающее страницу структуры компании в древовидной форме"""

    template_name = 'structure/structure_company.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # при открытии страницы стираются фильтры сортировки и поиска представления EmployeesView
        common_where_and_request_data.clear()
        return self.render_to_response(context)


class EmployeesView(View):
    """
    Представление отображающее список сотрудников с использованием фильтров и формы поиска.
    Изначально при переходе на страницу, по блоку отдела, используется:
     фильтр отдела - position,
     сортировка по id сотрудника в прямом порядке
    Поиск позволяет фильтровать сотрудников в форме поиска,
    а также искать по неполному совпадению значений полей.
    """

    paginate_by = 25

    def get(self, request, order_by: str, direction: str, position_id: int = None):

        # получаем данные из формы поиска и фильтры поиска для sql запроса если они есть
        form = SearchEmployeeForm(common_where_and_request_data.get('request_data', {'position': position_id}))
        where_for_sql = common_where_and_request_data.get('where_for_sql', '')

        # если нет фильтров sql запроса, но есть параметр position_id (переход по блоку отдела),
        # то фильтруем только по отделу и сохраняем фильтр
        if not where_for_sql and position_id:
            where_for_sql = f'WHERE position_id = {position_id}'
            common_where_and_request_data['where_for_sql'] = where_for_sql
            common_where_and_request_data['request_data'] = {'position': position_id}

        # меняем сортировку на обратную если условие верно
        if direction == 'descend':
            order_by += ' DESC'

        sql = f'SELECT ROW_NUMBER() OVER(ORDER BY {order_by}) AS num, * FROM structure_employee {where_for_sql} ORDER BY {order_by}'

        employees_list = Employee.objects.raw(sql)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'position_id': position_id,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'form': form,
        }

        return render(request, 'structure/department.html', context=context)

    def post(self, request, order_by: str, direction: str, position_id: int = None):
        form = SearchEmployeeForm(request.POST)
        where_for_sql = None  # переменная строки фильтров для sql запроса
        list_filters_for_sql = None  # переменная списка фильтров запроса
        position_id = request.POST.get('position', None)

        if form.is_valid():
            # получаем фильтры для sql запроса из request.POST и создаём словарь
            request_dict_from_the_search_key_list = {k: v for k, v in form.cleaned_data.items() if v and k != 'position'}
            list_filters_for_sql = [f'{k} LIKE "%{v}%"' for k, v in request_dict_from_the_search_key_list.items()]

        # если в форме есть фильтр по отделу, то добавляем его в список фильтров
        if position_id:
            list_filters_for_sql.insert(0, f'position_id = {position_id}')

        """ 
        если фильтров поиска не поступало, то словарь common_where_and_request_data очищается
        иначе в словарь заносятся фильтры под ключом where_for_sql и данные формы под ключом request_data 
        """
        if not list_filters_for_sql:
            common_where_and_request_data.clear()
        else:
            # создаём строку фильтра WHERE для sql запрос из списка фильтров
            where_for_sql = 'WHERE ' + ' AND '.join(list_filters_for_sql)
            common_where_and_request_data['where_for_sql'] = where_for_sql
            common_where_and_request_data['request_data'] = request.POST

        if direction == 'descend':
            order_by += ' DESC'

        sql = f'SELECT ROW_NUMBER() OVER(ORDER BY {order_by}) AS num, * FROM structure_employee {where_for_sql} ORDER BY {order_by}'
        employees_list = Employee.objects.raw(sql)
        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'position_id': position_id,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'form': form,
        }

        return render(request, 'structure/department.html', context=context)


@require_http_methods(['GET'])
def clear_search(request):
    """Функция для очистки полей формы поиска EmployeesView"""
    form = SearchEmployeeForm()
    return render(request, 'structure/search_form.html', context={'form': form})


def update_employee_details(request, pk, num):
    """Функция изменения данных сотрудника"""
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateEmployeeDetailForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            employee.num = num
            return render(request, 'structure/employee_detail.html', {'employee': employee})
    else:
        form = UpdateEmployeeDetailForm(instance=employee)
    return render(request, 'structure/partial_employee_update_form.html', {'employee': employee, 'form': form, 'num': num})


@require_http_methods(['GET'])
def employee_detail(request, pk, num):
    """Функция для возврата исходных данных, при отмене изменений данных сотрудника"""
    employee = get_object_or_404(Employee, pk=pk)
    employee.num = num
    return render(request, 'structure/employee_detail.html', {'employee': employee})


@require_http_methods(['DELETE'])
def delete_employee(request, pk):
    """Функция удаления сотрудника из базы данных (кнопка уволить)"""
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return HttpResponse()


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
