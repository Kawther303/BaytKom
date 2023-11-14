from django.contrib import admin
from .models import Room, Facility, RoomPic
from .models import Profile, Booking, Review


# Register your models here.
admin.site.register(Room)
admin.site.register(Facility)
admin.site.register(RoomPic)
admin.site.register(Booking)
admin.site.register(Profile)
admin.site.register(Review)

