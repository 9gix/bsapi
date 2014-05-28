from rest_framework import viewsets
from rest_framework import views
from rest_framework import response

from catalog.models import BookProfile
from catalog.serializers import BookProfileSerializer
from catalog import providers


class BookProfileViewSet(viewsets.ModelViewSet):
    model = BookProfile
    serializer_class = BookProfileSerializer



class SearchBook(views.APIView):
    model = BookProfile

    def get(self, request, format=None):
        query = self.request.QUERY_PARAMS.get('q', None)

        result_list = []

        book_list = providers.search(query)

        for book in book_list:
            result_list.append(BookProfile.objects.update_or_create(
                isbn13=book.isbn13,defaults=book.to_dict()))

        serializer = BookProfileSerializer(result_list, many=True)
        return response.Response(serializer.data)


search = SearchBook.as_view()
