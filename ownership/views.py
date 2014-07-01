from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from ownership.models import UserBook
from ownership.permissions import IsOwnerOrAdminElseReadOnly

class UserBookViewSet(viewsets.ModelViewSet):
    model = UserBook
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminElseReadOnly,
    )

    def pre_save(self, obj):
        obj.owner = self.request.user
