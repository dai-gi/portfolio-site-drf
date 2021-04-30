from django.urls import path
from app import views

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
]