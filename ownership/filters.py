import django_filters

from ownership.models import UserBook


class UserBookFilter(django_filters.FilterSet):
    isbn = django_filters.NumberFilter(name='book__isbn13')
    class Meta:
        model = UserBook
        fields = ['isbn']

