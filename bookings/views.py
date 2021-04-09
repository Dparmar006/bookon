from django.shortcuts import render, redirect

# utilities
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages
# model
from .models import Booking
from users.models import Customer, BookonUser
from services.models import Service


class BookingsListView(ListView):
    template_name = 'booking/listBooking.html'

    def get_queryset(self):
        self.customer = get_object_or_404(
            Customer, username=self.request.user.get_username())

        print(Booking.objects.filter(customer_name=self.customer))

        return Booking.objects.filter(customer_name=self.customer)


def book_service(request, slug):
    service = Service.objects.get(slug=slug)
    Booking.objects.create(service_name=service, customer_name=request.user)
    messages.success(request, "Service booked")
    return redirect("booking:listBookings")


def cancel_booking(request, slug):
    service = Service.objects.get(slug=slug)
    Booking.objects.get(service_name=service).delete()
    messages.error(request, "Service cancelled")
    return redirect("booking:listBookings")
