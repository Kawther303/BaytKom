
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Room
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

from .forms import UpdateUserForm,UpdateProfileForm
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

