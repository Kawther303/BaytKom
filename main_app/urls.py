from django.urls import path
from . import views
from .views import  profile
from .views import ChangePasswordView


urlpatterns = [
path('', views.home, name='home'),
path('about/',views.about,name='about'),
path('accounts/signup/', views.signup, name='signup'),
path('accounts/profile/', views.profile, name='profile'),
path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]