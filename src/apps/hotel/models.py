from django.db import models


class City(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
