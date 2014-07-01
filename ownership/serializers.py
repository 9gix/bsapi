from rest_framework import serializers

from ownership.models import UserBook


class UserBookSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
            view_name='userbook-detail',
            lookup_field='pk')
    book = serializers.SlugRelatedField(slug_field='isbn13')
    owner = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = UserBook
