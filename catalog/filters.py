import django_filters

from catalog.models import Book, Category

class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        return super(ListFilter, self).filter(qs, [value.split(","), 'in'])

class CategoryFilter(django_filters.FilterSet):
    with_owner = django_filters.BooleanFilter(
            action=lambda qs, val:
            qs.filter(book__owners__isnull=not val).distinct())
    class Meta:
        model = Category
        fields = ['with_owner']

class BookFilter(django_filters.FilterSet):
    isbn = django_filters.NumberFilter(name='isbn13')
    categories = ListFilter(name='categories__slug')
    with_owner = django_filters.BooleanFilter(
            action=lambda qs, val: qs.exclude(owners__isnull=val))
    class Meta:
        model = Book
        fields = ['isbn', 'categories', 'with_owner']
