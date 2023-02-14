import os
import configurations

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course4_proj.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")


configurations.setup()

app = Celery("course4_proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
