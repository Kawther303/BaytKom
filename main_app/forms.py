from django.forms import ModelForm
from .models import Facility

class FacilityForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
  class Meta:
    model = Facility
    fields = ['name', 'icon', 'description']