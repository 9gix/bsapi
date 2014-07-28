from django.shortcuts import render
from django.db.models import Q

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

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(Q(borrower_membership__user=user)|Q(owner_book__owner=user)).distinct()

    @action()
    def approve(self, request, pk=None):
        loanrequest = self.get_object()
        if not loanrequest.isApproved():
            loanrequest.approve()
            return Response({
                'status': loanrequest.status,
                'status_display': loanrequest.get_status_display()
            })
        else:
            return Response(
                    {'errors': 'request already been approved'},
                    status=status.HTTP_400_BAD_REQUEST)

    @action()
    def reject(self, request, pk=None):
        loanrequest = self.get_object()
        if not loanrequest.isRejected():
            loanrequest.reject()
            return Response({
                'status': loanrequest.status,
                'status_display': loanrequest.get_status_display()
            })
        else:
            return Response(
                    {'errors': 'request already been rejected'},
                    status=status.HTTP_400_BAD_REQUEST)
