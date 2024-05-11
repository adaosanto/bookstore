import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookStore.settings')

app = Celery('bookStore', broker_connection_retry_on_startup=True)

app.config_from_object('django.conf:settings', namespace='CELERY')

packages = [
    'bookStore'
]
packages.extend(settings.INSTALLED_APPS)
app.autodiscover_tasks(packages)
