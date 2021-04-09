from django.urls import path
from . import views


app_name = "booking"

urlpatterns = [
    path("", views.BookingsListView.as_view(), name="listBookings"),
    path("book/<str:slug>/", views.book_service, name="bookService"),
    path("cancel/<str:slug>/", views.cancel_booking, name="cancelService")
]
