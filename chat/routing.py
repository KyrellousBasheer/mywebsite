from django.urls import re_path

from . import consummers


websocket_urlpatterns = [
    re_path(r"ws/socket-server/", consummers.ChatConsummer.as_asgi())
]
