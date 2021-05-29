"""
ASGI config for real_time_graph project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddleware,AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from live_graphapp.routing import ws_urlPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_time_graph.settings')

# application = ProtocolTypeRouter({
#     'http':get_asgi_application(),
#     'websocket':AuthMiddleware(URLRouter(ws_urlPattern))
#
# })
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlPattern)),
})

