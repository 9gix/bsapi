from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from catalog.models import Book
from reservations.models import BookReservation
from comm.models import Conversation, ConversationMessage
from ownership.models import OwnerBook
from reviews.models import Review

class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class BookViewSet(viewsets.ModelViewSet):
    model = Book

class OwnerBookViewSet(viewsets.ModelViewSet):
    model = OwnerBook

class BookReservationViewSet(viewsets.ModelViewSet):
    model = BookReservation

class ConversationViewSet(viewsets.ModelViewSet):
    model = Conversation

class ConversationMessageViewSet(viewsets.ModelViewSet):
    model = ConversationMessage

class ReviewViewSet(viewsets.ModelViewSet):
    model = Review


