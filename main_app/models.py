from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


RoomType = (
  ('1', 'Sigle Room'),
  ('2', 'Double Room'),
  ('3', 'Shared Room'),
  ('4', 'Studio'),
  ('5', 'Suite'),
  ('6','Guest House'),
  ('7','Duplex')
)

class Facility(models.Model):
  name = models.CharField(max_length=100, default="")
  description = models.TextField(max_length=250)
  icon = models.ImageField(upload_to = "main_app/static/uploads", default="")


  def __str__(self):
    return self.name


  def get_absolute_url(self):
    return reverse('facilities_detail', kwargs={'pk': self.id})



# Create your models here.


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  full_name = models.CharField(max_length=100)
  user_type = models.CharField(choices=[('ADMIN', 'Admin'), ('RENTER', 'Renter')], max_length=10)
  address = models.TextField()
  phone_number = models.IntegerField(default=0)
  image = models.ImageField(upload_to='main_app/static/uploads', default='')
  def _str_(self):
    return self.user.username

class Room(models.Model):
  name = models.CharField(max_length=100)
  roomType = models.CharField(max_length=1, choices=RoomType, default=RoomType[0][0])
  image = models.ImageField(upload_to = "main_app/static/uploads", default="")
  size = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places= 2, max_digits= 5, default=0.00)
  description = models.TextField(max_length=250)
  country = models.CharField(max_length=100)    
  city = models.CharField(max_length=100)
  street = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  location = models.CharField(max_length=100)
  facilities = models.ManyToManyField(Facility)


  def __str__(self):
    return f"{self.name}"


  def get_absolute_url(self):
    return reverse('detail', kwargs={'room_id': self.id}) 














