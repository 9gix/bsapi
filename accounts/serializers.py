from rest_framework import serializers
from accounts.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField()

    class Meta:
        model = UserProfile
