from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from ownership.models import UserBook
from ownership.serializers import UserBookSerializer
from ownership.permissions import IsOwnerOrAdminElseReadOnly
from ownership.filters import UserBookFilter

class UserBookViewSet(viewsets.ModelViewSet):
    model = UserBook
    serializer_class = UserBookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminElseReadOnly,
    )
    filter_class = UserBookFilter

class MyBookViewSet(viewsets.ModelViewSet):
    model = UserBook
    serializer_class = UserBookSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrAdminElseReadOnly,
    )
    filter_class = UserBookFilter

    def get_queryset(self):
        user = self.request.user
        return UserBook.objects.filter(owner=user)
