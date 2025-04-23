from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.handlers.asgi import ASGIRequest
from django.db.models import F

from structure.consumers.distribution_consumers import \
    DistributionGroupConsumer
from structure.consumers.structure_consumers import StructureGroupConsumer
from structure.forms import UpdateEmployeeDetailForm
from structure.models import Employee, Position
from structure.permissions.staff_permissions import staff_required


def get_context(request: ASGIRequest, employee: Employee):
    channel_layer = get_channel_layer()
    employee_was_is_manager = employee.position.is_manager if employee.position else None
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
        context = {
            'employee': employee,
            'staff': staff_required(request.user),
        }
        employee_current_is_manager = employee.position.is_manager if employee.position else None
        if employee_current_is_manager or employee_was_is_manager:
            async_to_sync(channel_layer.group_send)(StructureGroupConsumer.group_name, {
                'type': 'group_message',
                'message': '',
            })
        if employee.position is None:
            async_to_sync(channel_layer.group_send)(DistributionGroupConsumer.group_name, {
                'type': 'group_message',
                'message': '',
            })
        return context
    return None
