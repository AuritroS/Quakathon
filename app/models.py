from typing import Iterable
from django.db import models
from geopy.geocoders import Nominatim

# Create your models here.


class Campus(models.Model):
    campus_title = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.campus_title


class Location(models.Model):
    address = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, null=True, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.address and (self.latitude is None or self.longitude is None):
            self.geocode()
        super().save(*args, **kwargs)

    def geocode(self):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(self.address)
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude

    def __str__(self) -> str:
        return self.address
    