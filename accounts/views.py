from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import viewsets
from rest_framework import permissions


from accounts.models import UserProfile
from accounts.permissions import IsAdminOrIsSelf
from accounts.serializers import (
        UserSerializer, UserProfileSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permission_classes = (
            permissions.DjangoModelPermissionsOrAnonReadOnly,
            IsAdminOrIsSelf,
    )
    serializer_class = UserSerializer

    def get_queryset(self):
        users = get_user_model().objects
        if self.request.user.is_staff:
            return users.all()
        else:
            return users.filter(id = self.request.user.id)

class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
