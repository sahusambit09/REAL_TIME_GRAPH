from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from django.urls import path
from .consumer import GraphConsumer

ws_urlPattern=[
    path('ws/polData/',GraphConsumer.as_asgi()),
]

