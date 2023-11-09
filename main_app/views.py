
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Room, Facility
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request,'about.html')


def rooms_index(request):
  rooms = Room.objects.all()
  return render(request, 'rooms/index.html', {'rooms': rooms})


class RoomCreate(LoginRequiredMixin, CreateView):
  model = Room
  fields = ['name', 'roomType', 'description', 'price', 'image', 'size', 'country', 'city', 'street', 'address', 'location']

class RoomUpdate(LoginRequiredMixin, UpdateView):
  model = Room
  fields = ['roomType', 'description', 'image', 'size', 'country', 'city', 'street', 'address', 'location']

class RoomDelete(LoginRequiredMixin, DeleteView):
  model = Room
  success_url = '/rooms/'


@login_required
def rooms_detail(request, room_id):
  room = Room.objects.get(id=room_id)
  return render(request, 'rooms/detail.html', {'room': room})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid User already available - please try other user',
      form.error_messages
  form = UserCreationForm()
  context = {'form': form,
  'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class FacilityList(LoginRequiredMixin, ListView):
  model = Facility

class FacilityDetail(LoginRequiredMixin, DetailView):
  model = Facility

class FacilityCreate(LoginRequiredMixin, CreateView):
  model =Facility
  fields = ['name', 'icon', 'description']

class FacilityUpdate(LoginRequiredMixin, UpdateView):
  model = Facility
  fields = ['name', 'icon', 'description']

class FacilityDelete(LoginRequiredMixin, DeleteView):
  model = Facility
  success_url = '/facilities/'
