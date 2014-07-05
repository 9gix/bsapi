from rest_framework import serializers

from catalog.models import Book


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="book-detail",
            lookup_field='isbn13')
    authors = serializers.SlugRelatedField(many=True, slug_field='name')
    publisher = serializers.SlugRelatedField(slug_field='name')
    categories = serializers.SlugRelatedField(many=True, slug_field='name')
    owners = serializers.RelatedField(many=True)

    class Meta:
        model = Book

    def get_identity(self, data):
        return data.get('isbn13')
