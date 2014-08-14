from rest_framework import serializers

from catalog.models import Book, Category


class ThumbnailField(serializers.ImageField):
    def to_native(self, value):

        # Patch
        # https://github.com/tomchristie/django-rest-framework/pull/1714

        request = self.context.get('request', None)
        try:
            return request.build_absolute_uri(value.url)
        except ValueError:
            return ""

class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="book-detail",
            lookup_field='isbn13')
    isbn = serializers.CharField(source='isbn13')
    authors = serializers.SlugRelatedField(many=True, slug_field='name')
    publisher = serializers.SlugRelatedField(slug_field='name',
            required=False)
    categories = serializers.SlugRelatedField(many=True, slug_field='name')
    owners = serializers.RelatedField(many=True)

    thumbnail = ThumbnailField()

    class Meta:
        model = Book
        exclude = ('isbn13',)

    def get_identity(self, data):
        return data.get('isbn13')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
