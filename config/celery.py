import os
import sys
from pathlib import Path

from celery import Celery
from django.core.management import execute_from_command_line

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# current_path = Path(__file__).parent.resolve()
# sys.path.append(str(current_path / "app"))
# execute_from_command_line(sys.argv)

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


