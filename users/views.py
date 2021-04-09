from django.shortcuts import render, redirect
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
# Forms
from .forms import CustomerCreationForm
from django.contrib.auth.forms import AuthenticationForm
# models
from .models import Owner


def home(request):
    return render(request, 'home.html')


def signoutPage(request):
    if logout(request):
        messages.success(request, "Logged out !")
    return redirect('user:customerSigninPage')


def serviceDashboard(request):
    return render(request, 'owner/serviceDashboard.html')


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
                return redirect('user:homePage')
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
                    messages.info(request, "You have been logged in...")
                    return redirect('user:homePage')
                else:
                    login(request, user)
                    messages.info(request, "You have been logged in...")
                    return redirect('user:serviceDashboard')
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
                return redirect('user:serviceDashboard')
            else:
                messages.error(request, "Some error occured !")
    else:
        form = CustomerCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'owner/owner-signup.html', context)
