from django.urls import path

from structure.consumers import (distribution_consumers, login_consumers,
                                 structure_consumers)

websocket_urlpatterns = [
    path('', login_consumers.Connection.as_asgi()),
    path('structure-company/', structure_consumers.StructureGroupConsumer.as_asgi()),
    path('recruit_distribution/', distribution_consumers.DistributionGroupConsumer.as_asgi()),
]
