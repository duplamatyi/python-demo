from django_selenium.livetestcases import SeleniumLiveTestCase
from django.core.urlresolvers import reverse
from src.apps.hotel.models import City, Hotel


class FunctionalTestCase(SeleniumLiveTestCase):

    def setUp(self):
        super(FunctionalTestCase, self).setUp()
        amsterdam = City.objects.create(code="AMS", name="Amsterdam")
        Hotel.objects.create(code="CAT", name="Ibis Amsterdam Airport", city=amsterdam)

    def test_hotel_list(self):
        self.driver.open_url(reverse('hotel_index'))
        self.assertEquals(self.driver.get_title(), 'Hotels')
        self.driver.type_in('input#city-typeahead', 'Amsterdam')
        self.driver.wait_element_present('div.tt-suggestion')
        self.driver.click('div.tt-suggestion a')
        self.driver.wait_element_present('li.hotel-list-item')
        self.assertEquals(self.driver.get_text('li.hotel-list-item'), 'Ibis Amsterdam Airport')
