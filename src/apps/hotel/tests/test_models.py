from django.test import TestCase
from src.apps.hotel.models import Hotel, City


class ModelsTestCase(TestCase):

    def setUp(self):
        amsterdam = City.objects.create(code="AMS", name="Amsterdam")
        Hotel.objects.create(code="CAT", name="Ibis Amsterdam Airport", city=amsterdam)

    def test_models_can_be_created(self):
        amsterdam = City.objects.get(name='Amsterdam')
        self.assertEqual(str(amsterdam), 'Amsterdam')
        hotel = Hotel.objects.get(city=amsterdam)
        self.assertEqual(str(hotel), 'Ibis Amsterdam Airport')
