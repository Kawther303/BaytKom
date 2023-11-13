from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Facility, RoomPic, Review
from .models import Booking, Room, Profile


class CreateUserForm(UserCreationForm):
  class Meta:
      model= User
      fields = ['username','email','password1','password2']



class FacilityForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
  class Meta:
    model = Facility
    fields = ['name', 'icon', 'description']

class RoomPicForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
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

# class SearchForm(ModelForm):
#   class Meta: #addional functionalty to access and use CBV
#     model = Room
#     fields = __all__

class ReviewForm(ModelForm):
  class Meta:
      model= Review
      fields = ['comment','date', 'room']