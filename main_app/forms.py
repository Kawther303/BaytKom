from django.forms import ModelForm
from .models import Facility, RoomPic

class FacilityForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
  class Meta:
    model = Facility
    fields = ['name', 'icon', 'description']

class RoomPicForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
  class Meta:
    model = RoomPic
    fields = ['RoomImages']
    