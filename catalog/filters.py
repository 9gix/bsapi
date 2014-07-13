import django_filters

from catalog.models import Book

class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        return super(ListFilter, self).filter(qs, [value.split(","), 'in'])

class BookFilter(django_filters.FilterSet):
    isbn = django_filters.NumberFilter(name='isbn13')
    categories = ListFilter(name='categories__slug')
    with_owner = django_filters.BooleanFilter(
            action=lambda qs, val: qs.filter(owners__isnull=not val))
    class Meta:
        model = Book
        fields = ['isbn', 'categories', 'with_owner']
