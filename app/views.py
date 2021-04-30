from rest_framework import generics
from .serializers import PostSerializer
from .models import Profile


class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializers = ProfileSerializer