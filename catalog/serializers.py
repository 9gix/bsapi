from rest_framework import serializers

from catalog.models import Book


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="book-detail",
            lookup_field='isbn13')
    authors = serializers.RelatedField(many=True)
    publisher = serializers.RelatedField()
    categories = serializers.RelatedField(many=True)

    class Meta:
        model = Book

    def get_identity(self, data):
        return data.get('isbn13')
