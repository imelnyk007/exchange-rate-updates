import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "exchange_rate_updates.settings"
)

application = get_asgi_application()
