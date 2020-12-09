from django.db import models

# Create your models here.
from users.models import Customer
from services.models import Service


class Booking(models.Model):
    # TODO: change CASCADE to Possibly PROTECTED in production
    service_name = models.OneToOneField(Service, on_delete=models.CASCADE)
    customer_name = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # finish_at = models.DateTimeField(null=True, blank=True, default=)
