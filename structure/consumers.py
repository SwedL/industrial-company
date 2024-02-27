import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Position


class Connection(WebsocketConsumer):
    def connect(self):
        self.accept()    # new

    def receive(self, text_data=None, bytes_data=None):
        position = {}  # словарь должностей и

        if text_data and 'type_message' in text_data:
            td = json.loads(text_data)
            if td['type_message'] == 'remove_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                current_employee = from_position.employee_set.all().first()
                current_employee.position = None
                current_employee.save()

            if td['type_message'] == 'appoint_manager':
                from_position = Position.objects.filter(id=td['from_position_id']).first()
                to_position = Position.objects.filter(id=td['to_position_id']).first()
                current_employee = from_position.employee_set.all().first()
                current_employee.position = to_position
                current_employee.save()
                print(current_employee)

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
