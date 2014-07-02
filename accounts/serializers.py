from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import UserProfile
from accounts.permissions import IsAdminOrSelf


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField()

    class Meta:
        model = UserProfile

class UserSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
            view_name="user-detail",
            lookup_field='username')
    books = serializers.RelatedField(many=True)
    communities = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'email',
                'password', 'books', 'communities')
        write_only_fields = ('password',)


    def validate_password(self, attr, source):
        password = attr[source]

        if len(password) < 6:
            raise serializers.ValidationError("Password at least 6 character")
        return attr

    def restore_object(self, attrs, instance=None):
        password = attrs.pop('password', None)

        if instance:
            user = instance
            # Update an existing user
            for key, val in attrs.items():
                setattr(user, key, val)
        else:
            # Create a new user
            user = User(**attrs)

        if password:
            user.set_password(password)

        return user
