from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from reservation.models import LoanRequest
from reservation.serializers import LoanRequestSerializer


class LoanRequestViewSet(viewsets.ModelViewSet):
    model = LoanRequest
    serializer_class = LoanRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @action()
    def approve(self, request, pk=None):
        loanrequest = self.get_object()
        if not loanrequest.isApproved():
            loanrequest.approve()
            return Response({'status': loanrequest.status})
        else:
            return Response(
                    {'errors': 'request already been approved'},
                    status=status.HTTP_400_BAD_REQUEST)

    @action()
    def reject(self, request, pk=None):
        loanrequest = self.get_object()
        if not loanrequest.isRejected():
            loanrequest.reject()
            return Response({'status': loanrequest.status})
        else:
            return Response(
                    {'errors': 'request already been rejected'},
                    status=status.HTTP_400_BAD_REQUEST)
