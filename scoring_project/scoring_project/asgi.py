"""
ASGI config for scoring_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoring_project.settings')
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from scoring import routing  # Update with your actual app name
from django.urls import path
from scoring import consumers  
# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoring_project.settings')

# Initialize Django before loading routing
django.setup()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # WebSocket URL pattern
            path('ws/score/<int:event_id>/', consumers.ScoreUpdateConsumer.as_asgi()),  # WebSocket path
        ])
    ),
})
