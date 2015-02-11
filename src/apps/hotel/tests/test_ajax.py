import json
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from src.apps.hotel.models import City, Hotel


class AjaxTestCase(TestCase):

    def setUp(self):
        setattr(self, 'client', Client())
        amsterdam = City.objects.create(code="AMS", name="Amsterdam")
        Hotel.objects.create(code="CAT", name="Ibis Amsterdam Airport", city=amsterdam)

    def test_hotel_city(self):
        client = getattr(self, 'client')
        response = client.get('%s?q=Amsterdam' % reverse('city'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(1, len(content))
        print content
        self.assertEqual('Amsterdam', content[0]['fields']['name'])

    def test_hotel_hotel(self):
        client = getattr(self, 'client')
        city_response = client.get('%s?q=Amsterdam' % reverse('city'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        city_content = json.loads(city_response.content)
        city_pk = city_content[0]['pk']
        hotel_response = client.get(
            reverse('hotel', kwargs={'city_pk': city_pk}),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(hotel_response.status_code, 200)
        hotel_content = json.loads(hotel_response.content)
        self.assertEqual(1, len(hotel_content))
        self.assertEqual('Ibis Amsterdam Airport', hotel_content[0]['fields']['name'])
