from __future__ import absolute_import

from celery import shared_task
from src import src_app

from celery.task import PeriodicTask
from django.core.management import call_command
from os.path import join
from django.conf import settings
from datetime import timedelta


# class ImportCities(PeriodicTask):
#     def run(self, **kwargs):
#         city_datasource = join(settings.IMPORT_DATASOURCE_DIR, 'city.csv')
#         hotel_datasource = join(settings.IMPORT_DATASOURCE_DIR, 'hotel.csv')
#         call_command('import', city_datasource, 'city')
#         call_command('import', hotel_datasource, 'hotel')


@src_app.task
def import_cities():
    city_datasource = join(settings.IMPORT_DATASOURCE_DIR, 'city.csv')
    hotel_datasource = join(settings.IMPORT_DATASOURCE_DIR, 'hotel.csv')
    call_command('import', city_datasource, 'city')
    call_command('import', hotel_datasource, 'hotel')
