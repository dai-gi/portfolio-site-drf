from rest_framework import serializers
from .models import Profile, Production

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'title', 'subtitle', 'name', 'twitter', 'github', 'programming', 'topimage', 'subimage')


class ProductionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Production
        fields = ('id', 'title', 'image', 'thumbnail', 'skill', 'github', 'url', 'created', 'description')