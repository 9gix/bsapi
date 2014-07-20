from django.shortcuts import render

from rest_framework import viewsets

from conversation.models import (
        Channel, ChannelMessage
)


class ChannelViewSet(viewsets.ModelViewSet):
    model = Channel

class ChannelMessageViewSet(viewsets.ModelViewSet):
    model = ChannelMessage

