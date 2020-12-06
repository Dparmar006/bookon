from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser

# Other apps 'service'
from services.models import Service

# Create your models here.


class BookonUser(AbstractUser):
    class Types(models.TextChoices):
        OWNER = "OWNER", "Owner"
        CUSTOMER = "CUSTOMER", "Customer "

    type = models.CharField(
        max_length=20, choices=Types.choices, default=Types.CUSTOMER
    )

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(type=BookonUser.Types.CUSTOMER)
        )


class OwnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=BookonUser.Types.OWNER)


class Customer(BookonUser):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = BookonUser.Types.CUSTOMER
        return super().save(*args, **kwargs)


class CustomerMore(models.Model):
    district = models.CharField(max_length=50)


class OwnerMore(models.Model):
    service = models.ForeignKey(
        Service, related_name="Owner of the service", on_delete=models.CASCADE
    )


class Owner(BookonUser):
    objects = OwnerManager()

    def more(self):
        return self.ownermore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = BookonUser.Types.OWNER
        return super().save(*args, **kwargs)
