from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Room, Facility, RoomPic
from .forms import FacilityForm
from .forms import RoomPicForm
import datetime


from django.contrib.auth.models import User
from .models import Room, Booking, Facility, Profile

from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpdateUserForm, UpdateProfileForm, BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})

def adminIndex(request, user_id):
    user = User.objects.get(id=user_id)
    print(user_id)
    return render(request, 'adminIndex.html', {'user': user})


class RoomCreate(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['name', 'roomType', 'description', 'price', 'image', 'size', 'country', 'city', 'street', 'address','location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RoomUpdate(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ['roomType', 'description', 'image', 'size', 'country', 'city', 'street', 'address', 'location']


class RoomDelete(LoginRequiredMixin, DeleteView):
    model = Room
    success_url = '/rooms/'


class BookCreate(CreateView):
    model = Booking
    fields = ['room', 'from_date', 'to_date', 'guest_name', 'guest_email', 'guest_mobile', 'price']
    success_url = '/rooms/'


# @login_required
# def rooms_showdetail(request, room_id):
#     room = Room.objects.get(id=room_id)
#     booking_form = BookingForm()
#     return render(request, 'rooms/showDetail.html', {'room': room, 'booking_form': booking_form})


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
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


class FacilityList(LoginRequiredMixin, ListView):
    model = Facility


class FacilityDetail(LoginRequiredMixin, DetailView):
    model = Facility



# room will display all the facility and have the form for adding new facility for specific image 
@login_required
def rooms_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    facility_form = FacilityForm()
    roompic_form = RoomPicForm()
    facilities_room_dosent_have = Facility.objects.exclude(id__in = room.facilities.all().values_list('id'))
    return render(request, 'rooms/detail.html', {'room':room, 'facility_form': facility_form, 'roompic_form': roompic_form, 'facilities': facilities_room_dosent_have })


def room_detail_alt(request, room_id):
    room = Room.objects.get(id=room_id)
    room_pic = RoomPic.objects.filter(room=room_id)
    # booking_form = BookingForm()
    context = {    
    'check': 0, 
    'check_in' :'',
    'check_out' :'' 
    }
    return render(request, 'detail_alt.html', {'room':room, 'context': context, 'room_pics':room_pic})


@login_required
def add_facility(request, room_id):
    form = FacilityForm(request.POST, request.FILES)
    if form.is_valid():
        new_facility = form.save(commit = False)
        new_facility.room_id = room_id
        new_facility.save()
    return redirect('detail', room_id =room_id) 


@login_required
def add_roompic(request, room_id):
    if request.method == 'POST':
        form = RoomPicForm(request.POST, request.FILES)  
        if form.is_valid():
            new_roompic = form.save(commit=False)
            new_roompic.room_id = room_id
            new_roompic.save()
            return redirect('detail', room_id=room_id)
    else:
        form = RoomPicForm()
    
    return render(request, 'add_roompic.html', {'form': form})




class FacilityUpdate(LoginRequiredMixin, UpdateView):
    model = Facility
    fields = ['name', 'icon', 'description']
    success_url = '/facilities/'

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


class FacilityCreate(LoginRequiredMixin, CreateView):
    model = Facility
    fields = ['name', 'icon', 'description']


class FacilityUpdate(LoginRequiredMixin, UpdateView):
    model = Facility
    fields = ['name', 'icon', 'description']


class FacilityDelete(LoginRequiredMixin, DeleteView):
    model = Facility
    success_url = '/facilities/'


@login_required
def booking_create(request, room_id):

    users = User.objects.get(username=request.user)
    room = Room.objects.get(id=room_id)
    booking_form = BookingForm()
    print('B_users:',users.id)
    user = Profile.objects.get(user_id=users.id)
    return render(request, 'booking/detail.html', {'room' : room, 'booking_form':booking_form, 'user':user} )

# @login_required
# def add_booking(request, room_id, user_id):
#   form = BookingForm(request.POST)
#   if form.is_valid():
#     new_booking = form.save(commit = False)
#     new_booking.room = room_id
#     new_booking.user = user_id
#     new_booking.price = request.POST['price']
#     new_booking.save()
#   return render(request, 'booking/confirmation.html', {'booking' : form} )
def add_booking(request, room_id, user_id):
    # user_id = user.id
    booking_price = request.POST['theprice']
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
    req = request
    return HttpResponse (f'<h2> confirm booking for {req} </h2>')



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
    country = request.POST['country_search']
    from_date = request.POST['check_in']
    to_date = request.POST['check_out']
    the_available_rooms= []

    rooms = Room.objects.filter(country=country)
    for room in rooms:
        if checkAvailable(room.id,from_date,to_date):
            the_available_rooms.append(room)
    return render(request, 'rooms/index.html', {'rooms': the_available_rooms , 'country':country ,'from_date': from_date, 'to_date':to_date   })
    # return HttpResponse(country)
def checkAvailability(request):
    context:[]
    room_id = request.GET['s_room_id']
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']
    check = checkAvailable(room_id,check_in,check_out)
    if (check == True):
        ch = 1
    else:
        ch = -1
    context = {
        'check':ch,
        'check_in' :check_in,
        'check_out' :check_out  
        }
    room = Room.objects.get(id=room_id)
    room_pic = RoomPic.objects.filter(room=room_id)
    return render(request, 'detail_alt.html', {'room':room, 'context': context, 'room_pics':room_pic})
#   return render(request,'detail_alt.html',{'R_check':check , 'R_check_in':check_in,'R_check_out':check_out  })

# render(request,'detail_alt.html',{'context':context} )
# return redirect(request,{'R_check':check , 'R_check_in':check_in,'R_check_out':check_out  })

@login_required
def user_Booking(request):

    context =[] 

    bookings = Booking.objects.all().filter(user=request.user)
    for book in bookings:
        room = Room.objects.filter(id=book.room.id)
        context.append({
        "booking" : book,
        "room": room[0]
    })    
    room = Room.objects.all()
    return render(request, 'booking/user_booking.html',{'context' : context})
  # return render(request, 'booking/user_booking.html', {'bookings': bookings , 'room':room})
  # return render(request, 'booking/user_booking.html', {'bookings': bookings})
  # bookings = Booking.objects.all()
  # return render(request, 'booking/user_booking.html', {'bookings': bookings})
