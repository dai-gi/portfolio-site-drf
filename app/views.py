from rest_framework import generics
from .serializers import ProfileSerializer, ProductionSerializer
from .models import Profile, Production


class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProductionView(generics.ListAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionDetailView(generics.RetrieveAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer