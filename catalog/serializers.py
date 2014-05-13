from rest_framework import serializers

from catalog.models import BookProfile


class BookProfileSerializer(serializers.ModelSerializer):
    authors = serializers.RelatedField(many=True)
    publisher = serializers.RelatedField()
    url = serializers.HyperlinkedIdentityField(view_name="bookprofile-detail")

    class Meta:
        model = BookProfile
