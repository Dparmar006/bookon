from django.db import models

from users.models import Owner
# utility
from django.shortcuts import reverse


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    like = models.IntegerField(blank=True, null=True)
    average_service_time = models.DurationField()
    owner = models.ForeignKey(Owner,  on_delete=models.CASCADE, default=1)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service:detailService", kwargs={"slug": self.slug})
