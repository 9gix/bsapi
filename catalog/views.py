from datetime import datetime

from haystack.inputs import Clean
from haystack.query import SearchQuerySet
from rest_framework import viewsets
from rest_framework import views
from rest_framework import response
from rest_framework import generics

from catalog.models import (
        Book, Publisher, Category, Author)
from catalog.serializers import BookSerializer
from catalog import providers


class BookViewSet(viewsets.ModelViewSet):
    """This endpoint will provide books information in our system.

    To use this API you have to provide the `isbn13` into the url. 

    - `/books/`
    - `/books/9780062073488/`
    - `/books/9781101161883/`
    """
    model = Book
    serializer_class = BookSerializer
    lookup_field = 'isbn13'


class BookProviderView(generics.ListAPIView):
    """This endpoint will search the books from all of the providers.

    To use this search API you have to provide the `q` query parameters

    - `/search/provider/?q=cakephp`
    - `/search/provider/?q=python`
    """
    model = Book
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.QUERY_PARAMS.get('q', None)

        result_list = []

        raw_data = providers.search(query)
        book_list = []
        for item in raw_data.get('items'):
            book_data = {}
            for k, v in item.get('volumeInfo').items():
                book_data[k] = v

            # Publisher
            publisher = book_data.get('publisher')
            if publisher:
                publisher, created = Publisher.objects.get_or_create(
                        name=book_data['publisher'])
                book_data['publisher'] = publisher.id

            # ISBN
            id_type_map = {
                    'ISBN_13': 'isbn13',
                    'ISBN_10': 'isbn10'
            }
            for identifier in book_data.get('industryIdentifiers', []):
                id_type = id_type_map.get(identifier.get('type'))
                book_data.update({id_type: identifier['identifier']})

            # Author
            authors = []
            for auth in book_data.get('authors',[]):
                author, created = Author.objects.get_or_create(name=auth)
                authors.append(author.id)
            book_data['authors'] = authors

            # Category
            categories = []
            for cat in book_data.get('categories',[]):
                category, created = Category.objects.get_or_create(name=cat)
                categories.append(category.id)
            book_data['categories'] = categories

            pubdate = book_data.get('publishedDate', '')
            try:
                clean_date = datetime.strptime(pubdate, "%Y-%m-%d")
            except ValueError as e:
                pass # ignore published date
            else:
                book_data['published_on'] = pubdate

            if book_data.get('isbn13'):
                book_list.append(book_data)

        book_list = [book for book in book_list if 'isbn13' in book]
        isbn13_list = [book['isbn13'] for book in book_list]
        queryset = Book.objects.select_related('publisher').filter(isbn13__in=isbn13_list)
        serializer = BookSerializer(queryset, data=book_list, many=True, allow_add_remove=True)
        if serializer.is_valid():
            serializer.save()
        return serializer.object


book_provider = BookProviderView.as_view()

class SearchView(generics.ListAPIView):
    """This endpoint will search the books recorded in our system.

    To use this search API you have to provide the `q` query parameters

    - `/search/?q=cakephp`
    - `/search/?q=python`
    """
    model = Book
    serializer_class = BookSerializer
    def get_queryset(self, *args, **kwargs):
        results = SearchQuerySet().filter(content=Clean(self.request.QUERY_PARAMS.get('q','')))

        # Open Bug: https://github.com/toastdriven/django-haystack/issues/985
        # isbn_list = results.values_list('isbn13', flat=True)
        # Patch to the issue 985
        isbn_list = [book.isbn13 for book in results]

        return self.model.objects.filter(isbn13__in=isbn_list)


search = SearchView.as_view()
