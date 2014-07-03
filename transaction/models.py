from django.db import models
from django.conf import settings

class Transaction(models.Model):
    book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL) #not sure about the foreign key, currently there are too many users defined. i.e. settings.AUTH_USER_MODEL, membership.user, accounts.UserProfile 
    lender = book.owner #not sure whether it is ok to do this
    transaction_date = models.DateField(auto_now_add = True)
    BOOK_RETURN_CHOICES = (
        ('UN', 'Unreturned'),
        ('RE', 'Returned'),
        ('LO', 'Lost'),
    )
    book_return = models.CharField(max_length = 2, choices = BOOK_RETURN_CHOICES, default = 'UN')

    def create_transaction(self):
    #this function should involve the transaction of credit, lender increase reputation
        self.book.current_holder = borrower
        self.book.owner.reputation.increase()
        

    def terminate_transaction(self):

        #lender edit the status of book_return
        if self.book_return == 'RE':
            self.book.current_holder = lender
        elif self.book_return == 'LO':
            #user should remove the page of book: self.book.delete()
            self.borrower.reputation.decrease()#since reputation is not merged, this one may show error