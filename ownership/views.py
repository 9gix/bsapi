from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from ownership.models import UserBook
from ownership.serializers import UserBookSerializer
from ownership.permissions import IsOwnerOrAdminElseReadOnly

class UserBookViewSet(viewsets.ModelViewSet):
    model = UserBook
    serializer_class = UserBookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminElseReadOnly,
    )

class MyBookViewSet(viewsets.ModelViewSet):
    model = UserBook
    serializer_class = UserBookSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrAdminElseReadOnly,
    )

    def get_queryset(self):
        user = self.request.user
        return UserBook.objects.filter(owner=user)
