from django.db import models

# Create your models here.
from users.models import Customer
from services.models import Service


class Booking(models.Model):
    # TODO: change CASCADE to Possibly PROTECTED in production
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    # finish_at = models.DateTimeField(null=True, blank=True, default=)

    def __str__(self):
        return f"{self.service_name.title}  booked by  {self.customer_name.first_name}"
