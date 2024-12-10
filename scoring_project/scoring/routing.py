from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/score/(?P<event_name>.+)/$', consumers.ScoreUpdateConsumer.as_asgi()),
]

