from django.db import models
from django.conf import settings
from communities.models import Membership

class Transaction(models.Model):
    book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL)
    transaction_date = models.DateField(auto_now_add = True)
    ON_LOAN = 1
    AVAILABLE = 0
    LOST = -1
    TRANSACTION_STATUS_CHOICES = (
        (ON_LOAN, 'On Loan'),
        (AVAILABLE, 'Available'),
        (LOST, 'Lost'),
    )
    transaction_status = models.SmallIntegerField(choices = TRANSACTION_STATUS_CHOICES, default = ON_LOAN)

#override the creation of Transaction 
    @classmethod
    def create(cls, **kwargs):
        new_transaction = cls(**kwargs)
        new_transaction.book.current_holder = new_transaction.borrower
        Membership.objects.all().get(user = new_transaction.book.owner).reputation.increase()
        return new_transaction
    

    def terminate_transaction(self):
        if self.transaction_status == LOST:
            #edit book's status
            Membership.objects.all().get(user = self.borrower).reputation.decrease()
