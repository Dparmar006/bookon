from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BookonUser(AbstractUser):

    class Types(models.TextChoices):
        OWNER = "OWNER", "Owner"
        CUSTOMER = "CUSTOMER", "Customer "

    type = models.CharField(max_length=20,
                            choices=Types.choices, default=Types.CUSTOMER)

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Customer(BookonUser):
    class Meta:
        proxy = True


class Owner(BookonUser):
    class Meta:
        proxy = True
