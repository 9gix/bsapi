from django.db import models
from django.conf import settings
from communities.models import Membership

class Transaction(models.Model):
    book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL)
    lender = book.owner
    transaction_date = models.DateField(auto_now_add = True)
    TRANSACTION_STATUS_CHOICES = (
        ('OL', 'On Loan'),
        ('AL', 'Available'),
        ('LO', 'Lost'),
    )
    transaction_status = models.CharField(max_length = 2, choices = TRANSACTION_STATUS_CHOICES, default = 'OL')

    @classmethod
    def create(cls, **kwargs):
        new_transaction = cls(**kwargs)
        new_transaction.book.current_holder = self.borrower
        Membership.objects.all().get(user = new_transaction.lender).reputation.increase()
        return new_transaction
    #override the creation of Transaction     

    def terminate_transaction(self):
        #after owner edit the transaction_status
        if self.transaction_status == 'AL':
            self.book.current_holder = self.lender
        elif self.transaction_status == 'LO':
            #edit book's status
            Membership.objects.all().get(user = self.borrower).reputation.decrease()
