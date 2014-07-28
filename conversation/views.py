from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from conversation.models import (
        Channel, Message
)
from conversation.serializers import (
        ChannelSerializer, MessageSerializer
)


class ChannelViewSet(viewsets.ModelViewSet):
    model = Channel
    serializer_class = ChannelSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )
