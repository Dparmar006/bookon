from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):

    genders = [('male', 'Male'),
               ('female', 'Female'),
               ('other', 'Others')
               ]
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name',
                  'username', 'email', 'phone', 'gender', 'password1', 'password2']
