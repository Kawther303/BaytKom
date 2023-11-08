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
  fields = ['name', 'roomType', 'description', 'image', 'size', 'price', 'country', 'city', 'street', 'address', 'location']


