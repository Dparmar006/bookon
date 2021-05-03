from django.db import models

from users.models import Owner
# utility
from django.shortcuts import reverse
from django.utils.text import slugify
from datetime import timedelta


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    like = models.IntegerField(blank=True, null=True)
    start_time = models.DurationField(blank=True, null=True)
    end_time = models.DurationField(blank=True, null=True)
    average_service_time = models.DurationField(default=timedelta(minutes=25))
    owner = models.ForeignKey(Owner,  on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("services:detailService", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # self.average_service_time = timedelta(
        #     minutes=cle)
        super(Service, self).save(*args, **kwargs)
