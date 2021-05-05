from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView

import datetime

from django.contrib.auth import authenticate, login, logout
# Forms
from .forms import CustomerCreationForm
from django.contrib.auth.forms import AuthenticationForm
# models
from .models import Owner, Customer
from bookings.models import Booking


class Home(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        self.customer = get_object_or_404(
            Customer, username=self.request.user.get_username())

        return Booking.objects.filter(customer_name=self.customer).order_by('start_time')


def signoutPage(request):
    if logout(request):
        messages.success(request, "Logged out !")
    return redirect('user:customerSigninPage')


def owner_dashboard(request):
    if request.method == 'POST':
        booking = Booking.objects.get(id=request.POST.get('order_id'))
        start_time = datetime.datetime.strptime(
            request.POST.get('service_schedule_date') + " " + request.POST.get('service_schedule_time'), "%Y-%m-%d %H:%M")
        booking.start_time = start_time
        booking.end_time = booking.start_time + \
            booking.service_name.average_service_time
        booking.save()
        messages.success(request,
                         f"You have scheduled {booking.customer_name}'s service at {start_time}")
        print(start_time, "post")
    print(request.user.type, " logged in")
    if(request.user.type == "OWNER"):
        all_bookings = Booking.objects.filter(
            service_name__owner=request.user).order_by('start_time')
        context = {'all_bookings': all_bookings}
    else:
        messages.error(request, "You can not access this page")
        return redirect("user:home_page")
    return render(request, 'owner/owner-dashboard.html', context)


def customerSignupPage(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST.get(
                'username'), password=request.POST.get('password1'))
            if user is not None:
                login(request, user)
                messages.success(request, "Account has been created")
                return redirect('user:home_page')
            else:
                messages.error(
                    request, "Couldn't create an account, Try again.")
    else:
        form = CustomerCreationForm()

    context = {
        'form': form,

    }
    return render(request, 'customer/customer-signup.html', context)


def customerSigninPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.type == 'CUSTOMER':
                    login(request, user)
                    messages.info(
                        request, f"Logged in, Welcome {user.first_name}")
                    return redirect('user:home_page')
                else:
                    login(request, user)
                    messages.info(
                        request, f"Logged in as Owner, Welcome {user.first_name}")
                    return redirect('user:owner_dashboard')
            else:
                messages.error(request, "Username or Password is wrong !")
        else:
            messages.error(request, "Username or Password is wrong !")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,

    }
    return render(request, 'customer/customer-signup.html', context)


# owner
def ownerSignupPage(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lasttname = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            gender = form.cleaned_data.get('gender')

            user = Owner.objects.create(username=username,
                                        email=email, first_name=firstname, last_name=lasttname, phone=phone, gender=gender)
            user.set_password(password1)
            user.save()
            if user is not None:
                login(request, user)
                messages.success(request, "Owner profile has been created !")
                return redirect('user:owner_dashboard')
            else:
                messages.error(request, "Some error occured !")
    else:
        form = CustomerCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'owner/owner-signup.html', context)
