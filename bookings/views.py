from django.shortcuts import render, redirect

# utilities
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
from django.utils import timezone
# model
from .models import Booking
from users.models import Customer
from services.models import Service


class BookingsListView(ListView):
    template_name = 'booking/listBooking.html'

    def get_queryset(self):
        self.customer = get_object_or_404(
            Customer, username=self.request.user.get_username())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todays_booking"] = Booking.objects.filter(
            customer_name=self.customer).filter(start_time__gte=datetime.datetime.now(tz=timezone.utc))
        context["object_list"] = Booking.objects.filter(
            customer_name=self.customer)

        return context


def book_service(request, slug):
    if(request.user.type == "OWNER"):
        messages.error(
            request, "Login with customer account to book a service")
    else:
        service = Service.objects.get(slug=slug)
        Booking.objects.create(service_name=service,
                               customer_name=request.user)

        messages.success(request, f"{service} has been booked")
    return redirect("home_page")


def cancel_booking(request, id):
    Booking.objects.get(id=id).delete()
    if(request.user.type == "OWNER"):
        messages.error(request, "Service has been declined")
        return redirect("user:owner_dashboard")
    messages.error(request, "Service cancelled")
    return redirect("booking:listBookings")
