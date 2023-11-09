from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),
  # Room url
  path('rooms/', views.rooms_index, name='index'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('accounts/signup/', views.signup, name='signup'),
  path('rooms/<int:room_id>/', views.rooms_detail, name='detail'),
  path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='rooms_update'),
  path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='rooms_delete'),
  path('rooms/<int:room_id>/booking/', views.BookCreate.as_view(), name='book_create'),

]