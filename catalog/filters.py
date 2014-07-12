import django_filters

from catalog.models import Book

class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        return super(ListFilter, self).filter(qs, [value.split(","), 'in'])

class BookFilter(django_filters.FilterSet):
    isbn = django_filters.NumberFilter(name='isbn13')
    categories = ListFilter(name='categories__slug')
    class Meta:
        model = Book
        fields = ['isbn', 'categories']
