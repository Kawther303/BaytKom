from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),
  path('rooms/', views.rooms_index, name='index'),
  path('rooms/create', views.RoomCreate.as_view(), name='room_create'),


]