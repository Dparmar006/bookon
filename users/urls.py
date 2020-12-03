from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="Base template"),
    path('signup/', views.signUpPage, name="Signup form for user"),
]
