from django import forms
from .models import Profile

class Profile(forms.ModelForm):
   class Meta:
    model = Profile
    fields = ['full_name', 'user_type', 'address', 'phone_number', 'image']