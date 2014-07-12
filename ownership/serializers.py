import logging

from rest_framework import serializers

from catalog.serializers import BookSerializer
from catalog.models import Book
from ownership.models import UserBook

logger = logging.getLogger(__name__)

class IsbnField(serializers.CharField):
    def from_native(self, data):
        try:
            book = Book.objects.get(isbn13=data)
        except Book.DoesNotExist:
            # TODO Future implementation:
            # when isbn is not in our database, it should search from
            # provider and save the book.
            logger.warning('Book Does Not Exist: ' + data)
            book = None
        return book

class UserBookSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
            view_name='userbook-detail',
            lookup_field='pk')
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    current_holder = serializers.SlugRelatedField(slug_field='username',
            read_only=True)
    book = BookSerializer(read_only=True)
    isbn = IsbnField(write_only=True,
            error_messages={'required': 'Book Not Found'})

    def restore_object(self, attrs, instance=None):
        attrs['book'] = attrs.pop('isbn', None)
        instance = super(UserBookSerializer, self).restore_object(attrs, instance)
        user = self.context['request'].user
        instance.owner = user
        instance.current_holder = user
        return instance

    class Meta:
        model = UserBook
