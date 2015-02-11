from django.contrib import admin
from .models import City, Hotel


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass