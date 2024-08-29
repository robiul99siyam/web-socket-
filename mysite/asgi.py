import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import app.routing as routher

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(
        routher.websocket_urlpatterns  
    )
})
