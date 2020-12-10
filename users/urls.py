from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('signup/', views.customerSignupPage, name="customerSignupPage"),
    path('signin/', views.customerSigninPage, name="customerSigninPage"),
    path('signout/', views.customerSignoutPage, name="customerSignoutPage"),
]
