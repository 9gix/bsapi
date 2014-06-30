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

def create_transaction():
    #this function should involve the transaction of credit, lender increase reputation
    ownership.UserBOok.current_holder = borrower

def terminate_transaction():
    #lender should be able to edit the status of book_return
    #if status change to lost, borrower reduces reputation, edit UserBook.current_holder