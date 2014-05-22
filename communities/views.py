from django.shortcuts import render
from rest_framework import viewsets
from communities.models import Community


class CommunityViewSet(viewsets.ModelViewSet):
    model = Community
