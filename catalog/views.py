import logging
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
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

logger = logging.getLogger(__name__)


def get_or_create_name(model, attrs):
    obj, created = model.objects.get_or_create(**attrs)
    return obj.name

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


            # ISBN
            id_type_map = {
                    'ISBN_13': 'isbn',
                    'ISBN_10': 'isbn10'
            }
            for identifier in book_data.get('industryIdentifiers', []):
                id_type = id_type_map.get(identifier.get('type'))
                book_data.update({id_type: identifier['identifier']})

            # Category
            categories = book_data.get('categories', [])
            categories = [dict(name=cat) for cat in categories]
            categories = [get_or_create_name(Category, cat) for cat in categories]
            book_data['categories'] = categories


            # Author
            authors = book_data.get('authors', [])
            authors = [dict(name=auth) for auth in authors]
            authors = [get_or_create_name(Author, auth) for auth in authors]
            book_data['authors'] = authors

            # Publisher
            publisher = book_data.get('publisher')
            publisher = get_or_create_name(Publisher, dict(name=publisher))
            book_data['publisher'] = publisher

            # Publication Date
            pubdate = book_data.get('publishedDate', '')
            try:
                clean_date = datetime.strptime(pubdate, "%Y-%m-%d")
            except ValueError as e:
                pass # ignore published date
            else:
                book_data['published_on'] = pubdate


            if book_data.get('isbn'):
                try:
                    book = Book.objects.get(isbn13=book_data.get('isbn13'))
                except ObjectDoesNotExist:
                    book = None

                serializer = self.serializer_class(book, data=book_data)
                if serializer.is_valid():
                    serializer.save()
                    book_list.append(serializer.object)
                else:
                    logger.warning(serializer.errors)
                    logger.warning(book_data)

        return book_list


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
