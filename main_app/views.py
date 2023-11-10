
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
import cgi
form = cgi.FieldStorage()
import datetime
from .models import Room, Booking,  Facility

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
# from .forms import Profile
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UpdateUserForm,UpdateProfileForm,BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


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



class BookCreate(CreateView):
  model = Booking
  fields = ['room', 'from_date', 'to_date', 'guest_name', 'guest_email', 'guest_mobile','price']
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
            return redirect('home')
        else:
            error_message = 'Invalid User already available - please try another username'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm()

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


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

@login_required
def booking_create(request, room_id):
  user_id = 1
  # select * from main_app_book where id = book_id
  room = Room.objects.get(id=room_id)
  booking_form = BookingForm()
  user = Profile.objects.get(id=user_id)

  # reward_book_doesnot_have= Reward.objects.exclude(id__in= book.rewards.all().values_list('id'))
  # room_available = Room.objects.exclude(id__in = room.booking.all())
  return render(request, 'booking/detail.html', {'room' : room, 'booking_form':booking_form, 'user':user})

@login_required
def add_booking(request, room_id, user_id):
  # user_id = user.id
  booking_price = 50
  form = BookingForm(request.POST)
  if form.is_valid():
    new_booking = form.save(commit = False)
    new_booking.room_id = room_id
    new_booking.user_id = user_id
    new_booking.price= booking_price
    new_booking.save()
  return redirect(to='home') 

@login_required
def booking_confirmation(request):
  user_id = 1 
  # booking_price = 50
  # form = BookingForm(request.POST)
  # if form.is_valid():
  #   new_booking = form.save(commit = False)
  #   new_booking.room_id = room_id
  #   new_booking.user_id = user_id
  #   new_booking.price= booking_price
  #   new_booking.save()
  return redirect(to='home') 

# to check if the room is available
def checkAvailable(room,check_in,check_out):
   the_list = []
   
   the_check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
   the_check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()
   booking_list = Booking.objects.filter(room=room)
   for booking in booking_list:
      if booking.from_date > the_check_out or booking.to_date <the_check_in:
         the_list.append(True)
      else:
         the_list.append(False)
   
   return all(the_list)

def getRooms(request):
  # form = BookingForm(request.POST)

  country = request.POST['country_search']
  from_date = request.POST['check_in']
  to_date = request.POST['check_out']
  the_available_rooms= []

  rooms = Room.objects.filter(country=country)
  for room in rooms:
     if checkAvailable(room.id,from_date,to_date):
        the_available_rooms.append(room)
  return render(request, 'rooms/index.html', {'rooms': the_available_rooms})
  # return HttpResponse(country)
   