from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name='about'),
  # Room url
  path('rooms/', views.rooms_index, name='index'),
  path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
  path('rooms/<int:room_id>/', views.rooms_detail, name='detail'),
  path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='rooms_update'),
  path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='rooms_delete'),

  # Facility
  # path('facilities/', views.ToyList.as_view(), name='facilities_index'),
  # path('facilities/<int:pk>/', views.ToyDetail.as_view(), name='facilities_detail'),
  # path('facilities/create/', views.ToyCreate.as_view(), name='facilities_create'),
  # path('facilities/<int:pk>/update/', views.ToyUpdate.as_view(), name='facilities_update'),
  # path('facilities/<int:pk>/delete/', views.ToyDelete.as_view(), name='facilities_delete'),

]