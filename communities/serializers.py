from rest_framework import serializers

from communities.models import Community, Membership

class CommunitySerializer(serializers.ModelSerializer):
    members = serializers.RelatedField(many=True)

    class Meta:
        model = Community

class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
