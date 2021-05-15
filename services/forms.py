from django import forms
from django.forms import widgets

# models
from .models import Service


class serviceRegistratingForm(forms.ModelForm):
    open_time = forms.DateTimeField(widget=widgets.DateInput)
    close_time = forms.DateTimeField(help_text="HH:MM",  required=False)

    class Meta:
        model = Service
        fields = '__all__'
        exclude = ('owner', 'like', 'slug')
