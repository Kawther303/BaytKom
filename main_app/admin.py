from django.contrib import admin

from .models import Room, Facility
from .models import  Profile,Booking

# Register your models here.
admin.site.register(Room)
admin.site.register(Facility)
admin.site.register(Booking)
admin.site.register(Profile)
