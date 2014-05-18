from django.shortcuts import render

from rest_framework import viewsets

from comm.models import (
        Conversation, ConversationMessage
)


class ConversationViewSet(viewsets.ModelViewSet):
    model = Conversation

class ConversationMessageViewSet(viewsets.ModelViewSet):
    model = ConversationMessage

