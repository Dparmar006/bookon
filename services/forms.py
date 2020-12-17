from django import forms

# models
from .models import Service


class serviceRegistratingForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ('owner', 'like', 'slug')
