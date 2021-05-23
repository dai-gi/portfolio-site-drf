from django.urls import path
from app import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('production/', views.ProductionView.as_view(), name='production'),
    path('production/<str:pk>/', views.ProductionDetailView.as_view(), name='production-detail'),
]