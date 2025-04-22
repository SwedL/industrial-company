from channels.generic.websocket import WebsocketConsumer


class Connection(WebsocketConsumer):
    """ Соединение группы для страницы '' """
    def connect(self):
        print("server says connected")
        self.accept()  # new

    def receive(self, text_data=None, bytes_data=None):
        self.send("server sends Welcome")

    def disconnect(self, code):
        print("server says disconnected")
