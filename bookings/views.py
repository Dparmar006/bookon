from django.shortcuts import render

# utilities
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
# model
from .models import Booking
from users.models import Customer, BookonUser


class BookingsListView(ListView):
    template_name = 'booking/listBooking.html'

    def get_queryset(self):
        self.customer = get_object_or_404(
            Customer, username=self.request.user.get_username())

        print(Booking.objects.filter(customer_name=self.customer))

        return Booking.objects.filter(customer_name=self.customer)
