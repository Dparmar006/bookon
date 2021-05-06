from django.urls import path
from . import views

app_name = "user"
urlpatterns = [

    path('signup/', views.customerSignupPage, name="customerSignupPage"),
    path('ownersignup/', views.ownerSignupPage, name="ownerSignupPage"),
    path('signin/', views.customerSigninPage, name="customerSigninPage"),
    path('signout/', views.signoutPage, name="signoutPage"),
    # dashboard
    path('dashboard/', views.owner_dashboard, name="owner_dashboard"),


]
