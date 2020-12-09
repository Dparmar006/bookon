from django.db import models

from users.models import Owner
# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    like = models.IntegerField(blank=True, null=True)
    average_service_time = models.DurationField()
    shop_name = models.CharField(max_length=50, null=True, blank=True)
    shop_description = models.CharField(max_length=250, null=True, blank=True)
    owner = models.ForeignKey(Owner,  on_delete=models.CASCADE, default=1)
