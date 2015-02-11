from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

    def setUp(self):
        setattr(self, 'client', Client())

    def test_index_view_should_return_200(self):
        client = getattr(self, 'client')
        response = client.get(reverse('hotel_index'))
        self.assertEqual(response.status_code, 200)
