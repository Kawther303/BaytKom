from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Room, Facility, RoomPic
from .forms import FacilityForm
from .forms import RoomPicForm
from .forms import ReviewForm
from .forms import *
import datetime
from django.contrib.auth.views import PasswordResetView

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
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



@login_required
def rooms_index(request):
    rooms = Room.objects.all()
    profile = Profile.objects.filter(user_id=request.user.id)
    if (profile):
        user = profile[0]
    else:
        user=''
    return render(request, 'rooms/index.html', {'rooms': rooms, 'user':user})

# @login_required
# def rooms_adminindex(request):
#     rooms = Room.objects.all()
#     profile = Profile.objects.filter(user_id=request.user.id)
#     if (profile):
#         user = profile[0]
#     else:
#         user=''
#     return render(request, 'rooms/index.html', {'rooms': rooms, 'user':user})


def adminIndex(request, user_id):
    # user = User.objects.get(id=user_id)
    profile = Profile.objects.filter(user_id=request.user.id)
    if (profile):
        user = profile[0]
    else:
        user=''
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
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid User already available - please try another username'
    form = CreateUserForm()
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
    room_pic = RoomPic.objects.filter(room=room_id)
    facilities_room_dosent_have = Facility.objects.exclude(id__in = room.facilities.all().values_list('id'))
    return render(request, 'rooms/detail.html', {'room':room, 'facility_form': facility_form, 'roompic_form': roompic_form, 'facilities': facilities_room_dosent_have, 'room_pic':room_pic })


def room_detail_alt(request, room_id):
    room = Room.objects.get(id=room_id)
    room_pic = RoomPic.objects.filter(room=room_id)
    context = {    
    'check': 0, 
    'check_in' :'',
    'check_out' :'' 
    }
    return render(request, 'detail_alt.html', {'room':room, 'context': context, 'room_pic':room_pic})


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

# class RoomPicDetail(LoginRequiredMixin, DetailView):


#     model = RoomPic
#     fields = ['RoomPic']

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
    context = {
    'check_in' : request.GET['book_check_in'],
    'check_out' : request.GET['book_check_out'],
    'nights': request.GET['nights'],
    'price' : request.GET['price_id'] 
    }
    email = User.objects.get(username=request.user)
    room = Room.objects.get(id=room_id)
    booking_form = BookingForm()

    user = Profile.objects.get(user_id=email.id)

    return render(request, 'booking/detail.html', {'room' : room, 'booking_form':booking_form, 'user':user ,'context':context ,'email':email} )



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


@login_required
def booking_confirmation(request):
    return render(request, 'booking/booking_confirmation_email.html')

@login_required
def add_booking(request, room_id, user_id):
 room = Room.objects.filter(id=room_id)
 the_room = room[0]

 users = User.objects.get(username=request.user)
 user = Profile.objects.get(user_id=users.id)
 form = BookingForm(request.POST)
 check_room = checkAvailable(room_id,request.POST['from_date'],request.POST['to_date']);
 if check_room == True:
  if form.is_valid():
    new_booking = form.save(commit = False)
    new_booking.room_id = room_id
    new_booking.user_id = user_id
    new_booking.save()
    
    booking = {
         "new_booking":new_booking,
         "room" : the_room
     }

        # Send confirmation email to the user       
    subject = 'Booking Confirmation'
    message = render_to_string('booking/booking_confirmation_email.html', {

            'user': user,
            'room': room,
            'booking': new_booking,
        })
    from_email = 'djangoemail2002@gmail.com'
    to_email = [user.user.email]  # Assuming user has an email field

    print(to_email)
    try:
          send_mail(subject, message, from_email, to_email, fail_silently=False)
          print("Email sent successfully")
    except BadHeaderError as e:
            print(f"Invalid header found. Email not sent. Error: {e}")

    # return redirect(to='home')
    return render(request, 'booking/confirmation.html', {'booking' : booking} ) 
  else:
    return HttpResponse ('<h3>booking is having issue please retry again!</h3>') 
 else:
    return HttpResponse ('<h3>looks that the room is already booked check other days !!</h3>')   



@login_required
def booking_confirmation(request):
    req = request
    return HttpResponse (f'<h2> confirm booking for {req} </h2>')




# to check if the room is available
def checkAvailable(room,check_in,check_out):
    the_list = []  
    print('check_in:',check_in )
    print('check_out:',check_out )
    print('roommmmmmmmmmmmmmmmm:',room)
    the_check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
    the_check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()
    booking_list = Booking.objects.filter(room_id=room,status='A')
    print ('booking_list',booking_list)

    for booking in booking_list:
        if booking.from_date > the_check_out or booking.to_date <the_check_in:
            the_list.append(True)
        else:
            the_list.append(False)
    return all(the_list)


def getRooms(request):
    search= request.POST["searchBy"] 
    country = request.POST['country_search']
    from_date = request.POST['check_in']
    to_date = request.POST['check_out']
    the_available_rooms= []
    if search == 'country':
        rooms = Room.objects.filter(country__icontains=country)
    elif search == 'city':
        rooms = Room.objects.filter(city__icontains=country)
    else:
        rooms = Room.objects.filter(name__icontains=country) 

    for room in rooms:
        if checkAvailable(room.id,from_date,to_date):
            the_available_rooms.append(room)
    return render(request, 'rooms/index.html', {'rooms': the_available_rooms ,'search':search ,'country':country ,'from_date': from_date, 'to_date':to_date   })


def checkAvailability(request):
    context:[]
    room_id = request.GET['s_room_id']
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']

    print('room_id',room_id)
    print('check_in',check_in)
    print('check_out',check_out)

    check = checkAvailable(room_id,check_in,check_out) 
    print('check', check )
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


@login_required
def user_Booking(request):
    context =[] 
    bookings = Booking.objects.all().filter(user=request.user)
    
    for book in bookings:
        room = Room.objects.filter(id=book.room.id)
        # review_form = ReviewForm()
        context.append({
        "booking" : book,
        "room": room[0],
        # "review_form": review_form
    })    
    room = Room.objects.all()
    return render(request, 'booking/user_booking.html',{'context' : context})


@login_required
def cancel_Booking(request,booking):
    Booking.objects.filter(id=booking).update(status='C')
    return redirect(to='user_booking')

@login_required
def room_Booking(request):

    context =[] 
    rooms = Room.objects.filter(user=request.user.id)
    print("ussser:",request.user.id)
    print("roooms:",rooms)
    r = 0
    b = 0
    for room in rooms:   
        bookings = Booking.objects.all().filter(room=room.id)
        print("boook:",bookings)
        for booking in bookings:
            context.append({  
            "booking" : booking,
            "room": room
            })  


    return render(request, 'booking/room_booking.html',{'context' : context})


# Update profile information
from .forms import ProfileForm

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_update.html'
    success_url = ''

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.image = self.request.FILES.get('image')  
        profile.save()
        return super().form_valid(form)

# class ReviewList(LoginRequiredMixin, ListView):
#     model = Review
    


# class ReviewCreate(LoginRequiredMixin, CreateView):
#     model = Review
#     fields = ['comment', 'date']

#     def form_valid(self, form):
#         form.instance.room_id = self.request.room_id
#         return super().form_valid(form)



# @login_required
# def add_review(request, room_id):
#     print('room_id', room_id)
#     room = Room.objects.get(id=room_id)
#     print('fff', room)
#     # room = rooms[0]

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print('userrrrrrrrrrr', request.user.id)
#             new_review = form.save(commit=False)
#             new_review.room_id = room_id
#             new_review.user_id = request.user.id
#             new_review.save()
#             return render('add_review', {'room' : room, 'form': form})
#     else:
#         form = ReviewForm()
    
#         return render(request, 'add_review.html', {'room' : room, 'form': form})


@login_required
def room_review(request, room_id):
    room = Room.objects.get(id=room_id)
    reviews = Review.objects.filter(room_id=room_id)

    review_form = ReviewForm()
    return render(request, 'rooms/room_review.html', {'room':room, 'review_form': review_form, 'reviews': reviews})



@login_required
def add_review(request, room_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit = False)
        new_review.room_id = room_id
        new_review.user_id = request.user.id
        new_review.save()
    return redirect('room_review', room_id= room_id) 

    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')

