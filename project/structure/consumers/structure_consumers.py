import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db.models import F

from structure.consumers import distribution_consumers
from structure.models import Position
from structure.permissions.staff_permissions import staff_required


class StructureGroupConsumer(WebsocketConsumer):
    """ Соединение группы для страницы 'structure-company/' """
    group_name = "staff_group"
    distribution_group_name = distribution_consumers.DistributionGroupConsumer.group_name

    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        if text_data and 'type_message' in text_data:
            td = json.loads(text_data)
            # если в сообщении 'remove_manager', сотрудник становится без должности,
            # а вакансия в данной должности открывается
            if td['type_message'] == 'remove_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                current_employee = from_position.employee_set.first()
                current_employee.position = None
                current_employee.save()
                Position.objects.filter(id=td['from_position_id']).update(vacancies=F('vacancies') + 1)

                async_to_sync(self.channel_layer.group_send)(
                    self.distribution_group_name, {
                        "type": "group_message",
                        "message": '',
                    }
                )
            # если в сообщении 'appoint_manager', то сотруднику присваивается новая должность,
            # вакансия закрывается у новой должности и открывается у старой
            if td['type_message'] == 'appoint_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                Position.objects.filter(id=td['from_position_id']).update(vacancies=F('vacancies') + 1)
                to_position = Position.objects.filter(id=td['to_position_id']).first()
                Position.objects.filter(id=td['to_position_id']).update(vacancies=F('vacancies') - 1)
                current_employee = from_position.employee_set.first()
                current_employee.position = to_position
                current_employee.save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {
                "type": "group_message",
                "message": '',
            }
        )

    def group_message(self, event):
        message = self.get_positions()
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

    def get_positions(self):
        positions = {}  # словарь где key = position_id, value = ФИО сотрудника

        # наполняем словарь руководящими должностями и их ФИО
        for position_obj in Position.objects.filter(is_manager=True):
            employee = position_obj.employee_set.first()
            if employee:
                manager_name = f'{employee.last_name} {employee.first_name[0]}.{employee.patronymic[0]}.'
                positions[str(position_obj.id)] = manager_name
        data = {
            'positions': positions,
            'permission': staff_required(self.scope['user']),
        }

        return data
