from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'', include('src.apps.hotel.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '', url(r'^__debug__/', include(debug_toolbar.urls)),
    )
