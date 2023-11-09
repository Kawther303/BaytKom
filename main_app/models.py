from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=100)
  user_type = models.CharField(choices=[('admin', 'Admin'), ('renter', 'Renter')], max_length=10)
  address = models.TextField()
  phone_number = models.CharField(max_length=15)
  image = models.ImageField(upload_to='main_app/static/uploads', default='')
  def __str__(self):
    return self.user.username
  