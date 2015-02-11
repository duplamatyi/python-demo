import os
from os.path import join
import inspect
from django.test import TestCase
from django.core.management import call_command
from src.apps.hotel.models import City, Hotel


class ImportTestCase(TestCase):

    def setUp(self):
        setattr(self, 'test_dir', os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

    def test_city_import(self):
        data_source = join(getattr(self, 'test_dir'), 'data/city.csv')
        call_command('import', data_source, 'city')
        self.assertEqual(6, City.objects.count())

    def test_hotel_import(self):
        data_source = join(getattr(self, 'test_dir'), 'data/city.csv')
        call_command('import', data_source, 'city')
        data_source = join(getattr(self, 'test_dir'), 'data/hotel.csv')
        call_command('import', data_source, 'hotel')
        self.assertEqual(196, Hotel.objects.count())
