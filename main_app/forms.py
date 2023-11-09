
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
  class Meta:
    model =Room
    fields = ['roomType']

TYPES=(
  ('A','ADMIN'),
  ('R', 'RENTER')
)

class Profile(forms.ModelForm):
   class Meta:
    model = Profile
    fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']


class UpdateUserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']
      username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
      email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


class UpdateProfileForm(forms.ModelForm):
      full_name = forms.CharField(max_length=100, required=True)
      user_type = forms.ChoiceField(choices= TYPES, required=True)
      address = forms.CharField(max_length=100)
      phone_number = forms.IntegerField(max_value=20)
      image = forms.ImageField()
      # class Meta:
      #  model = Profile
      #  fields = ['full_name', 'user_type', 'address', 'phone_number', 'image' ]

