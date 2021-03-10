from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("", views.ServiceListingView.as_view(), name="listServices"),
    path("<slug>/", views.ServiceDetail.as_view(), name="detailService"),
    path("register/service/", views.serviceRegistration,
         name="serviceRegistration"),
]
