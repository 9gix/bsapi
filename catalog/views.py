from rest_framework import viewsets
from catalog.models import BookProfile
from catalog.serializers import BookProfileSerializer


class BookProfileViewSet(viewsets.ModelViewSet):
    model = BookProfile
    serializer_class = BookProfileSerializer
