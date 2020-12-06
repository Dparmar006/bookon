from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    like = models.IntegerField(blank=True, null=True)
    averageServiceTime = models.IntegerField(blank=True, null=True)
