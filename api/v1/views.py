from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions
from api import permissions as custom_permissions

from catalog.models import BookProfile
from reservations.models import BookReservation
from comm.models import Conversation, ConversationMessage
from ownership.models import Book
from reviews.models import Review

class UserViewSet(viewsets.ModelViewSet):
    model = User
    permission_classes = (permissions.IsAdminUser,)

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class BookProfileViewSet(viewsets.ModelViewSet):
    model = BookProfile

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


