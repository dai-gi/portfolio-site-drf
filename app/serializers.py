from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'title', 'subtitle', 'name', 'twitter', 'github', 'programming', 'introduction', 'topimage', 'subimage')