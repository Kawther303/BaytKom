from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Define the home view
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request,'about.html')

def rooms_index(request):
  rooms = Room.objects.all()
  return render(request, 'rooms/index.html', {'rooms': rooms})

class RoomCreate(CreateView):
  model = Room
  fields = ['name', 'roomType', 'description', 'price', 'image', 'size', 'country', 'city', 'street', 'address', 'location']

class RoomUpdate(UpdateView):
  model = Room
  fields = ['roomType', 'description', 'image', 'size', 'country', 'city', 'street', 'address', 'location']

class RoomDelete(DeleteView):
  model = Room
  success_url = '/rooms/'

def rooms_detail(request, room_id):
  room = Room.objects.get(id=room_id)
  return render(request, 'rooms/detail.html', {'room': room})



