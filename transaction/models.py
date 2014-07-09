from django.db import models
from django.conf import settings
from communities.models import Membership

class TransactionManager(models.Manager):
    def create_transaction(self, **kwargs):
        new_transaction = self.create(**kwargs)
        new_transaction.book.current_holder = new_transaction.borrower
        Membership.objects.get(user = new_transaction.book.owner).reputation.increase()
        return new_transaction

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

    objects = TransactionManager()
    

    def report_loss(self):
        Membership.objects.get(user = self.borrower).reputation.decrease()
