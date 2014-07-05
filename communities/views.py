from django.shortcuts import render

from rest_framework import viewsets

from communities.models import Community
from communities.models import Membership
from communities.serializers import CommunitySerializer
from communities.serializers import MembershipSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    model = Community
    serializer_class = CommunitySerializer

class MembershipViewSet(viewsets.ModelViewSet):
    model = Membership
    serializer_class = MembershipSerializer
