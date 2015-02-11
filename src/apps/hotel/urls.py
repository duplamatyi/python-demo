from django.conf.urls import patterns, include, url
from . import ajax, views

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='hotel_index'),
    url(r'^city/$', ajax.CityView.as_view(), name='city'),
    url(r'^city/(?P<city_pk>\d+)/hotel/$', ajax.HotelView.as_view(), name='hotel'),
)
