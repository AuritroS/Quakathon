from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Location

@receiver(pre_save, sender=Location)
def geocode_address(sender, instance, **kwargs):
    if instance.address and (instance.latitude is None or instance.longitude is None):
        instance.geocode()
