from django.shortcuts import render

from rest_framework import viewsets

from reservation.models import LoanRequest


class LoanRequestViewSet(viewsets.ModelViewSet):
    model = LoanRequest
