from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.dev_settings')

src_app = Celery('src')

src_app.config_from_object('celeryconfig')
src_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
