from django.urls import path
from . import views
from .views import  profile
from .views import ChangePasswordView


urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),

  path('rooms_list/', views.rooms_index, name='index_list'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('accounts/signup/', views.signup, name='signup'),
  
 
  
  path('accounts/profile/', views.profile, name='profile'),
  path('password-change/', ChangePasswordView.as_view(), name='password_change'),
  
    # Room url
  path('rooms/<int:room_id>/', views.rooms_detail, name='detail'),
  path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='rooms_update'),
  path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='rooms_delete'),

  # Facility
  path('facilities/', views.FacilityList.as_view(), name='facilities_index'),
  path('facilities/<int:pk>/', views.FacilityDetail.as_view(), name='facilities_detail'),
  path('facilities/create/', views.FacilityCreate.as_view(), name='facilities_create'),
  path('facilities/<int:pk>/update/', views.FacilityUpdate.as_view(), name='facilities_update'),
  path('facilities/<int:pk>/delete/', views.FacilityDelete.as_view(), name='facilities_delete'),


  #Booking
  path('rooms/', views.getRooms, name='index'),
  path('booking/<int:room_id>/', views.booking_create, name='booking_create'),
  path('booking/<int:room_id>/<int:user_id>/add_booking/',views.add_booking, name='add_booking') ,
  path('booking/<int:room_id>/add_booking/confirmation',views.booking_confirmation, name='booking_confirmation') ,
  path('booking/user_booking/',views.user_Booking, name='user_booking') ,
    # path('booking/<int:user_id>/user_booking/',views.user_Booking, name='user_booking') ,
  path('booking/check/',views.checkAvailability,name='check_availability'),
  #  path('booking/<int:room_id>/check/',views.checkAvailability,name='check_availability'),
]
