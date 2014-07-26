from django.shortcuts import render

from rest_framework import viewsets

from conversation.models import (
        Channel, Message
)


class ChannelViewSet(viewsets.ModelViewSet):
    model = Channel

class MessageViewSet(viewsets.ModelViewSet):
    model = Message

