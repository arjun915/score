from django.urls import re_path
from . import consumers

# websocket_urlpatterns = [
#     re_path(r'^ws/django_channels/$', MyConsumer.as_asgi()),
# ]
websocket_urlpatterns = [
    re_path(r'^ws/score/$', consumers.ScoreUpdateConsumer.as_asgi()),
]


