import django_filters

from communities.models import Membership


class MembershipFilter(django_filters.FilterSet):
    username = django_filters.CharFilter('user__username')
    class Meta:
        model = Membership
        fields = ['username', ]
