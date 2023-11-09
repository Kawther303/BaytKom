from django.contrib import admin

from .models import Room, Facility
from .models import  Profile
# Register your models here.
admin.site.register(Room)
admin.site.register(Facility)

admin.site.register(Profile)
