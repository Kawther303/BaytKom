from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Facility, RoomPic
from .models import Booking, Room, Profile, Review


class CreateUserForm(UserCreationForm):
  class Meta:
      model= User
      fields = ['username','email','password1','password2']



class FacilityForm(ModelForm):

  class Meta:
    model = Facility
    fields = ['name', 'icon', 'description']

class RoomPicForm(ModelForm):

  class Meta:
    model = RoomPic
    fields = ['roomImages']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']


class UpdateProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=[('admin', 'Admin'), ('customer', 'Customer')])

    class Meta:
        model = Profile
        fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class BookingForm(ModelForm):

  class Meta: #addional functionalty to access and use CBV
    model = Booking
    fields = ['from_date', 'to_date', 'guest_name','guest_email','guest_mobile','comment','price']


class ReviewForm(ModelForm):
  class Meta:
      model= Review
      fields = ['comment','date', 'rating']