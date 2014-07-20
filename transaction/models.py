from django.db import models
from django.conf import settings
from communities.models import Membership


class Transaction(models.Model):
    loan_request = models.OneToOneField('reservation.LoanRequest', null=True)
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} | Owner: {} -> Borrower: {} | {}".format(
                self.loan_request.owner_book.book.isbn13,
                self.loan_request.owner_book.owner.username,
                self.loan_request.borrower_membership.user.username,
                self.transaction_date)
