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


  # Facility
  path('facilities/', views.FacilityList.as_view(), name='facilities_index'),
  # path('facilities/<int:facility_id>/', views.facilities_detail, name='detail'),



  path('facilities/<int:pk>/', views.FacilityDetail.as_view(), name='facilities_detail'),
  path('facilities//<int:room_id>/add_facility', views.add_facility, name='add_facility'),
  path('facilities/<int:pk>/update/', views.FacilityUpdate.as_view(), name='facilities_update'),
  path('facilities/<int:pk>/delete/', views.FacilityDelete.as_view(), name='facilities_delete'),
    # assosiate a facility with a room
  path('rooms/<int:room_id>/assoc_facility/<int:facility_id>/', views.assoc_facility, name='assoc_facility'),

    # unassosiate a facility with a room
  path('rooms/<int:room_id>/unassoc_facility/<int:facility_id>/', views.unassoc_facility, name='unassoc_facility'),

]