from rest_framework import serializers

from catalog.serializers import BookSerializer
from ownership.models import UserBook


class UserBookSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
            view_name='userbook-detail',
            lookup_field='pk')
    owner = serializers.SlugRelatedField(slug_field='username')
    current_holder = serializers.SlugRelatedField(slug_field='username')
    book = BookSerializer()

    class Meta:
        model = UserBook
