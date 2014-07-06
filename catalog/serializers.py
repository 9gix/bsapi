from rest_framework import serializers

from catalog.models import Book


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="book-detail",
            lookup_field='isbn13')
    isbn = serializers.CharField(source='isbn13')
    authors = serializers.SlugRelatedField(many=True, slug_field='name',
            required=False)
    publisher = serializers.SlugRelatedField(slug_field='name',
            required=False)
    categories = serializers.SlugRelatedField(many=True, slug_field='name',
            required=False)
    owners = serializers.RelatedField(many=True)

    class Meta:
        model = Book
        exclude = ('isbn13',)

    def get_identity(self, data):
        return data.get('isbn13')
