"""bookon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from users.views import Home
from users.views import home_page

urlpatterns = [
    path('home/', Home.as_view(), name="home_page2"),
    path('', home_page, name="home_page"),
    path('admin/', admin.site.urls),

    path('user/', include('users.urls', namespace="user")),

    path('services/', include('services.urls', namespace="services")),
    path('bookings/', include('bookings.urls', namespace="bookings")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
