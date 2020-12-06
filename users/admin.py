from django.contrib import admin

from .models import Customer, Owner, BookonUser
# Register your models here.
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(BookonUser)
