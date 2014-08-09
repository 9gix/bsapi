from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    model = Transaction
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated, )
