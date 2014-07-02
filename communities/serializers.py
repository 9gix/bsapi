from rest_framework import serializers

from communities.models import Community

class CommunitySerializer(serializers.ModelSerializer):
    members = serializers.RelatedField(many=True)

    class Meta:
        model = Community
