from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Booking, Room, Profile

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
    class Meta:
        model = Booking
        fields = ['from_date', 'to_date', 'guest_name', 'guest_email', 'guest_mobile']