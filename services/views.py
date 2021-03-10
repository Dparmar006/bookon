
# utilities
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib import messages
# forms
from .forms import serviceRegistratingForm
# models
from .models import Service


def generate_slug(name):
    return name.lower().strip().replace(" ", "-")


@login_required
def serviceRegistration(request):
    # TODO: duplication of the slug
    if request.method == 'POST':
        form = serviceRegistratingForm(request.POST)
        if form.is_valid():
            service = form.save()
            service_name = form.cleaned_data.get('title')
            # service = Service.objects.get()
            print(service)
            messages.success(request, "Service added")
            return redirect("services:listServices")

    else:
        form = serviceRegistratingForm()
    context = {'form': form}
    return render(request, 'service/serviceRegistration.html', context)


class ServiceListingView(LoginRequiredMixin,  ListView):
    model = Service
    template_name = 'service/listServices.html'


class ServiceDetail(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'service/detailService.html'
