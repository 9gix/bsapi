from django.shortcuts import render

from rest_framework import viewsets

from conversation.models import (
        Channel, Message
)
from conversation.serializers import (
        ChannelSerializer, MessageSerializer
)


class ChannelViewSet(viewsets.ModelViewSet):
    model = Channel
    serializer_class = ChannelSerializer

class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    serializer_class = MessageSerializer
