from rest_framework import renderers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny


@api_view(('GET',))
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        'registration': reverse('user-registration', request=request,
            format=format),
        'users': reverse('user-list', request=request,
            format=format),
        'communities': reverse('community-list', request=request,
            format=format),
        'memberships': reverse('membership-list', request=request,
            format=format),
        'transactions': reverse('transaction-list', request=request,
            format=format),
        'book': reverse('book-list', request=request,
            format=format),
        'user-books': reverse('userbook-list', request=request,
            format=format),
        'my-books': reverse('mybook-list', request=request,
            format=format),
        'search-book-online': reverse('search-provider', request=request,
            format=format),
        'search-book-in-system': reverse('search', request=request,
            format=format),
        'categories' : reverse('category-list', request=request,
            format=format),
        'reservation' : reverse('loanrequest-list', request=request,
            format=format),
    })

