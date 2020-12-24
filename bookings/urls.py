from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path("", views.BookingsListView.as_view(), name="listBookings")
]
