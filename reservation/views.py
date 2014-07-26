from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from reservation.models import LoanRequest
from reservation.serializers import LoanRequestSerializer


class LoanRequestViewSet(viewsets.ModelViewSet):
    model = LoanRequest
    serializer_class = LoanRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
