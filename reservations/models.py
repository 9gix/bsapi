from django.db import models

class BookReservation(models.Model):

    # all class attributes/variable
    CANCELLED = -1
    PENDING = 0
    CONFIRMED = 1

    STATUS_CHOICES = (
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
    )


    # all database fields
    book = models.ForeignKey('ownership.Book')
    borrower = models.ForeignKey('auth.User')
    borrow_on = models.DateField()
    due_on = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
