
# utilities
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
# forms
from .forms import serviceRegistratingForm
# models
from .models import Service


@login_required
def serviceRegistration(request):
    if request.method == 'POST':
        form = serviceRegistratingForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = serviceRegistratingForm()
    context = {'form': form}
    return render(request, 'service/serviceRegistration.html', context)


class ServiceListingView(ListView):
    model = Service
    template_name = 'service/listServices.html'


class ServiceDetail(DetailView):
    model = Service
    template_name = 'service/detailService.html'
