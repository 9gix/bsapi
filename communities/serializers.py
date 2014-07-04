from rest_framework import serializers

from communities.models import Community, Membership

class CommunitySerializer(serializers.ModelSerializer):
    members = serializers.RelatedField(many=True)

    class Meta:
        model = Community

class MembershipSerializer(serializers.ModelSerializer):
    reputation = serializers.SlugRelatedField(
            slug_field='value', read_only=True)

    class Meta:
        model = Membership
        fields = ('community', 'user', 'reputation', 'is_moderator')
