from django.core.handlers.asgi import ASGIRequest
from django.core.paginator import Paginator
from django.db.models import Q, QuerySet
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber

from structure.forms import SearchEmployeeForm
from structure.models import Employee
from structure.permissions.staff_permissions import staff_required


class EmployeesViewService:
    def get_employees_list(self, order_by: str, direction: str) -> QuerySet:
        """ Функция фильтрует Employee QuerySet согласно заполненным полям формы SearchEmployeeForm,
            возвращает пронумерованный и отсортированный queryset """

        # если условие верно сортировка меняется на обратную
        if direction == 'descend':
            order_by = '-' + order_by

        employees_list = Employee.objects.filter(
            Q(last_name__contains=f'{self.common_form_data["last_name"]}') &
            Q(first_name__contains=f'{self.common_form_data["first_name"]}') &
            Q(patronymic__contains=f'{self.common_form_data["patronymic"]}')
        ).select_related('position')

        # дополнительная фильтрация, если в форме есть фильтр по отделу, дате трудоустройства или зарплате
        if self.common_form_data['position_id']:
            employees_list = employees_list.filter(position_id=self.common_form_data['position_id'])
        elif self.common_form_data['employment_date']:
            employees_list = employees_list.filter(employment_date=self.common_form_data['employment_date'])
        elif self.common_form_data['salary']:
            employees_list = employees_list.filter(salary=self.common_form_data['salary'])

        return employees_list.order_by(order_by).annotate(num=Window(expression=RowNumber(), order_by=[order_by]))

    def get_context_for_get_request(
            self,
            request: ASGIRequest,
            order_by: str,
            direction: str,
            position_id: str,
    ) -> dict:
        # если переход впервые - по блоку отдела, то фильтрация по position_id и занесение фильтра в common_form_data
        if not request.GET.get('page') and position_id:
            self.common_form_data.clear()
            self.common_form_data['position_id'] = position_id

        form = SearchEmployeeForm(self.common_form_data)

        employees_list = self.get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': self.common_form_data,
            'title': self.title,
            'staff': staff_required(request.user),
        }
        return context

    def get_context_for_post_request(self, request: ASGIRequest, order_by: str, direction: str) -> dict:
        form = SearchEmployeeForm(request.POST)

        # обновление словаря common_form_data
        if form.is_valid():
            self.common_form_data.update(form.cleaned_data)

        employees_list = self.get_employees_list(order_by, direction)

        paginator = Paginator(employees_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': self.common_form_data,
            'title': self.title,
            'staff': staff_required(request.user),
        }
        return context
