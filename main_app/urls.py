from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import profile
from .views import ChangePasswordView

urlpatterns = [

  path('', views.home, name='home'),
  path('about/',views.about,name='about'),

  path('rooms_list/', views.rooms_index, name='index_list'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('accounts/signup/', views.signup, name='signup'),

  
#     profile
    path('accounts/signup/', views.signup, name='signup'),    
    path('accounts/profile/', views.profile, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
  
# booking
    path('rooms/', views.getRooms, name='index'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('booking/<int:room_id>/', views.booking_create, name='booking_create'),
    path('booking/<int:room_id><int:user_id>/add_booking/', views.add_booking, name='add_booking'),
    path('booking/<int:room_id>/add_booking/confirmation', views.booking_confirmation, name='booking_confirmation'),



# room
    # Room url
  path('rooms_list/', views.rooms_index, name='index_list'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('rooms/<int:room_id>/', views.rooms_detail, name='detail'),

  path('rooms/<int:room_id>/alt/', views.room_detail_alt, name='room_detail_alt'),


  path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='rooms_update'),
  path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='rooms_delete'),
  path('rooms/<int:room_id>/add_roompic', views.add_roompic, name='add_roompic'),

    # Facility
  path('facilities/', views.FacilityList.as_view(), name='facilities_index'),
  path('facilities/<int:pk>/', views.FacilityDetail.as_view(), name='facilities_detail'),
  path('facilities/<int:room_id>/add_facility', views.add_facility, name='add_facility'),
  path('facilities/<int:pk>/update/', views.FacilityUpdate.as_view(), name='facilities_update'),
  path('facilities/<int:pk>/delete/', views.FacilityDelete.as_view(), name='facilities_delete'),
  path('facilities/create/', views.FacilityCreate.as_view(), name='facilities_create'),



  #Booking
  path('rooms/', views.getRooms, name='index'),
  path('booking/<int:room_id>/', views.booking_create, name='booking_create'),
  path('booking/<int:room_id>/<int:user_id>/add_booking/',views.add_booking, name='add_booking') ,
  path('booking/<int:room_id>/add_booking/confirmation',views.booking_confirmation, name='booking_confirmation') ,
  path('booking/user_booking/',views.user_Booking, name='user_booking') ,
    # path('booking/<int:user_id>/user_booking/',views.user_Booking, name='user_booking') ,
  path('room/check/',views.checkAvailability,name='check_availability'),
  #  path('booking/<int:room_id>/check/',views.checkAvailability,name='check_availability'),

    # assosiate a facility with a room
  path('rooms/<int:room_id>/assoc_facility/<int:facility_id>/', views.assoc_facility, name='assoc_facility'),
    # unassosiate a facility with a room
  path('rooms/<int:room_id>/unassoc_facility/<int:facility_id>/', views.unassoc_facility, name='unassoc_facility'),
]

