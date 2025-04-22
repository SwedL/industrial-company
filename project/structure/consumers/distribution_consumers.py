import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class DistributionGroupConsumer(WebsocketConsumer):
    """ Соединение группы для страницы 'recruit_distribution/' """
    group_name = "distribution_group"

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
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "group_message", "message": 'update_data'}
        )

    # Receive message from room group
    def group_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
