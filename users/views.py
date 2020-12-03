from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'base.html')


def signUpPage(request):
    return render(request, 'users/user-signup.html')
