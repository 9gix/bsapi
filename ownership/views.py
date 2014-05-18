from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from ownership.models import Book
from ownership.permissions import IsOwnerOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    model = Book
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, 
    )

    def pre_save(self, obj):
        obj.owner = self.request.user
