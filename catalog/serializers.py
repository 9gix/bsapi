from rest_framework import serializers

from catalog.models import BookProfile


class BookProfileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="bookprofile-detail")

    class Meta:
        model = BookProfile

    def get_identity(self, data):
        return data.get('isbn13')
