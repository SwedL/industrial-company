from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('', consumers.Connection.as_asgi()),
]
