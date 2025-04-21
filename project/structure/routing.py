from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('', consumers.Connection.as_asgi()),
    path('structure-company/', consumers.GroupConsumer.as_asgi()),
]
