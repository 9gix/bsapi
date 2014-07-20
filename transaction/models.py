from django.db import models
from django.conf import settings
from communities.models import Membership


class Transaction(models.Model):
    book = models.ForeignKey('ownership.UserBook')
    borrow_membership = models.ForeignKey('communities.Membership')
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} | Owner: {} -> Borrower: {} | {}".format(
                self.book.book.isbn13,
                self.book.owner,
                self.borrow_membership.user.username,
                self.transaction_date)
