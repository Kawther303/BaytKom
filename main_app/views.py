
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Room, Facility
from .forms import FacilityForm
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


# room will display all the facility and have the form for adding new facility for specific image 
@login_required
def rooms_detail(request, room_id):
  room = Room.objects.get(id=room_id)
  facility_form = FacilityForm()
  facilities_room_dosent_have = Facility.objects.exclude(id__in = room.facilities.all().values_list('id'))
  return render(request, 'rooms/detail.html', {'room':room, 'facility_form': facility_form, 'facilities': facilities_room_dosent_have })


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

@login_required
def add_facility(request, room_id):
  form = FacilityForm(request.POST)
  if form.is_valid():
    new_facility = form.save(commit = False)
    new_facility.room_id = room_id
    new_facility.save()
  return redirect('detail', room_id =room_id) 

class FacilityUpdate(LoginRequiredMixin, UpdateView):
  model = Facility
  fields = ['name', 'icon', 'description']

class FacilityDelete(LoginRequiredMixin, DeleteView):
  model = Facility
  success_url = '/facilities/'


@login_required
def assoc_facility(request, room_id, facility_id):
  # Add this facility_id with the room selected (room_id)
  Room.objects.get(id=room_id).facilities.add(facility_id)
  return redirect('detail', room_id=room_id)

@login_required
def unassoc_facility(request, room_id, facility_id):
  # remove this facility_id with the room selected (room_id)
  Room.objects.get(id=room_id).facilities.remove(facility_id)
  return redirect('detail', room_id=room_id)