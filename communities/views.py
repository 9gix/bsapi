from django.shortcuts import render

from rest_framework import viewsets

from communities.models import Community
from communities.serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    model = Community
    serializer_class = CommunitySerializer
