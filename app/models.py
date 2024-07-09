from typing import Iterable
from django.db import models
from geopy.geocoders import Nominatim

# Create your models here.

class Profile(models.Model):
    degree = models.CharField(max_length=255, null=True)
    course = models.CharField(max_length=255, null=True)
    dob = models.DateTimeField()


class Location(models.Model):
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    users = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    campus = models.CharField(max_length=255, null=True)
    duration = models.TimeField(null=True)
    type = models.CharField(max_length=255, null=True)
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

class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    duration = models.TimeField(null=True)
    

    