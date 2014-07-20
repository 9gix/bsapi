from django.db import models
from django.conf import settings
from communities.models import Membership


class Transaction(models.Model):
    loan_request = models.OneToOneField('reservation.LoanRequest')
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} transacted at {}".format(
                self.loan_request,
                self.transaction_date)
