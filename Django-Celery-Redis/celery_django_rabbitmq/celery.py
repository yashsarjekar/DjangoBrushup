from celery import Celery
import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django_rabbitmq.settings')

app = Celery('celery_django_rabbitmq')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
