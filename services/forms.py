from django import forms
from django.forms import widgets

# models
from .models import Service


class serviceRegistratingForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        exclude = ('owner', 'like', 'slug')
