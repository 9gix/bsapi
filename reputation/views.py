from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import views
from rest_framework import status
from rest_framework import response
from rest_framework import generics
from rest_framework.views import APIView

from reputation.models import Reputation
from reputation.serializers import ReputationSerializer

class ReputationViewSet(viewsets.ModelViewSet):
    model = Reputation
