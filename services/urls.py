from django.urls import path, re_path
from . import views

app_name = "services"

urlpatterns = [
    re_path(r'^$', views.ServiceListingView.as_view(), name="listServices"),
    path("<slug>/", views.ServiceDetail.as_view(), name="detailService"),
    path("register/service/", views.serviceRegistration,
         name="serviceRegistration"),
]
