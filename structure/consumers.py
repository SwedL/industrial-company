import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Position


class JoinAndLeave(WebsocketConsumer):
    def connect(self):
        # print("server says connected")
        self.accept()    # new

    def receive(self, text_data=None, bytes_data=None):
        print("server says client message received: ", text_data)

        position = {}
        for i in Position.objects.filter(is_manager=True):
            employee = i.employee_set.all().first()
            manager_name = f'{employee.last_name} {employee.first_name[0]}.{employee.patronymic[0]}.'
            position[i.id-1] = manager_name
        data = {
            "position": position,
        }
        if text_data and "type_message" in text_data:
            td = json.loads(text_data)
            print(td)
        self.send(json.dumps(data))
        # self.send("Server sends Welcome")

    def disconnect(self, code):
        print("server says disconnected")


# class GroupConsumer(WebsocketConsumer):
#     room_group_name = "staff_group"
#     # room_name = "update_date"
#
#     def connect(self):
#         print("server says connected")
#         self.accept()  # new
#
#     def receive(self, text_data=None, bytes_data=None):
#         print("server says client message received: ", text_data)
#         text_data = json.loads(text_data)
#         print(text_data)
#         type_message = text_data.get("type_message", None)
#         position = {}
#         if type_message == "remove_manager":
#             print(type_message, text_data)
#             data = text_data.get("data", None)
#             position_id = Position.objects.filter(id=int(data["position_id"])).first()
#             position_id.employee_set.all().first().position = None
#
#         for i in Position.objects.filter(is_manager=True):
#             employee = i.employee_set.all().first()
#             manager_name = f'{employee.last_name} {employee.first_name[0]}.{employee.patronymic[0]}.'
#             position[i.id] = manager_name
#         data = {
#             "position": position,
#         }
#         self.send(json.dumps(data))
#
#     def disconnect(self, code):
#         print("server says disconnected")

    # def staff_message(self, event):
    #     message = event["message"]
    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({"message": message}))
