from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Booking

from .models import Room, Profile 



class UpdateProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']
    user_type = forms.ChoiceField(choices=[('admin', 'Admin'), ('customer', 'Customer')], required=True)

# from .models import Room




# class RoomForm(ModelForm):
#   class Meta:
#     model =Room
#     fields = ['roomType']

class Profile(forms.ModelForm):
   class Meta:
    model = Profile
    fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']


class UpdateUserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']
      username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
      email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))



class BookingForm(ModelForm):
  class Meta: #addional functionalty to access and use CBV
    model = Booking
    fields = ['from_date', 'to_date', 'guest_name','guest_email','guest_mobile','comment']

# class SearchForm(ModelForm):
#   class Meta: #addional functionalty to access and use CBV
#     model = Room
#     fields = __all__