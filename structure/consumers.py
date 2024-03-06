import json

from channels.generic.websocket import WebsocketConsumer
from django.db.models import F

from .models import Position


class Connection(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        position = {}  # словарь где key = position_id, value = ФИО сотрудника

        if text_data and 'type_message' in text_data:
            td = json.loads(text_data)
            # если в сообщении снятие с руководящей должности, сотрудник становится без должности,
            # а вакансия в данной должности открывается
            if td['type_message'] == 'remove_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                current_employee = from_position.employee_set.all().first()
                current_employee.position = None
                current_employee.save()
                Position.objects.filter(id=td['from_position_id']).update(vacancies=F('vacancies') + 1)

            # если в сообщении переназначение должности, то сотруднику присваивается новая должность,
            # вакансия закрывается у новой должности и открывается у старой
            if td['type_message'] == 'appoint_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                Position.objects.filter(id=td['from_position_id']).update(vacancies=F('vacancies') + 1)
                to_position = Position.objects.filter(id=td['to_position_id']).first()
                Position.objects.filter(id=td['to_position_id']).update(vacancies=F('vacancies') - 1)
                current_employee = from_position.employee_set.all().first()
                current_employee.position = to_position
                current_employee.save()

        # наполняем словарь руководящими должностями и их ФИО
        for i in Position.objects.filter(is_manager=True):
            if i.employee_set.all().exists():
                employee = i.employee_set.all().first()
                manager_name = f'{employee.last_name} {employee.first_name[0]}.{employee.patronymic[0]}.'
                position[i.id] = manager_name
        data = {
            'position': position,
            'permission': self.scope['user'].has_perm('structure.change_employee'),
        }
        self.send(json.dumps(data))

    def disconnect(self, code):
        print('server says disconnected')
