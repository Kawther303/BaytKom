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
  ('6','Guest House')
)


# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=100)
  roomType = models.CharField(max_length=1, choices=RoomType, default=RoomType[0][0])
  image = models.ImageField(upload_to = "main_app/static/uploads", default="")
  size = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField(max_length=250)
  country = models.CharField(max_length=100)    
  city = models.CharField(max_length=100)
  street = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  location = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name}"
