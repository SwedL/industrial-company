"""
ASGI config for ic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import structure.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ic.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': asgi_application,
    'websocket':
        AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(structure.routing.websocket_urlpatterns)
            ),
        )
})
