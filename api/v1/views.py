from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions
from rest_framework.decorators import action, link, api_view
from rest_framework.response import Response
from rest_framework import status
from api import permissions as custom_permissions

from accounts.models import UserProfile
from accounts.permissions import IsAdminOrIsSelf
from accounts.serializers import UserSerializer, UserProfileSerializer 
from catalog.models import BookProfile
from catalog.serializers import BookProfileSerializer
from reservations.models import BookReservation
from comm.models import Conversation, ConversationMessage
from ownership.models import Book
from reviews.models import Review

class UserViewSet(viewsets.ModelViewSet):
    model = User
    permission_classes = (IsAdminOrIsSelf,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(id = self.request.user.id)

class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class BookProfileViewSet(viewsets.ModelViewSet):
    model = BookProfile
    serializer_class = BookProfileSerializer

class BookViewSet(viewsets.ModelViewSet):
    model = Book
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly, 
    )

    def pre_save(self, obj):
        obj.owner = self.request.user

class BookReservationViewSet(viewsets.ModelViewSet):
    model = BookReservation

class ConversationViewSet(viewsets.ModelViewSet):
    model = Conversation

class ConversationMessageViewSet(viewsets.ModelViewSet):
    model = ConversationMessage

class ReviewViewSet(viewsets.ModelViewSet):
    model = Review


