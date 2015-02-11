import six
from django.views.generic import ListView
from django.db.models import Q
from braces.views import JSONResponseMixin, AjaxResponseMixin
from .models import City, Hotel


class CityView(JSONResponseMixin, AjaxResponseMixin, ListView):
    model = City

    def get_ajax(self, request, *args, **kwargs):
        setattr(self, 'query', request.GET.get('q', ''))
        cities = self.get_queryset()

        return self.render_json_object_response(cities, fields=('name',))

    def get_queryset(self):
        terms = getattr(self, 'query').split()
        q_objects = Q()
        for term in terms:
            q_objects = q_objects | Q(name__icontains=term)

        return self.model.objects.filter(q_objects).order_by('name').only('name')


class HotelView(JSONResponseMixin, AjaxResponseMixin, ListView):
    model = Hotel

    def get_ajax(self, request, *args, **kwargs):
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

        hotels = self.get_queryset()

        return self.render_json_object_response(hotels, fields=('name',))

    def get_queryset(self):

        return self.model.objects.filter(city__pk=getattr(self, 'city_pk')).order_by('name').only('name')
