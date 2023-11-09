from django.urls import path
from . import views
from .views import  profile
from .views import ChangePasswordView


urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),

  path('rooms/', views.rooms_index, name='index'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('accounts/signup/', views.signup, name='signup'),

  path('rooms/booking/', views.BookCreate.as_view(), name='book_create'),
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

]
