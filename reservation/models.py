from django.db import models


class BookRequestStatus:
    PENDING = 0
    APPROVED = 1
    REJECTED = -1


class UserBookRequest(models.Model):

    _REQUEST_STATUS = (
        (BookRequestStatus.PENDING, 'Waiting for owner approval'),
        (BookRequestStatus.APPROVED, 'Request approved'),
        (BookRequestStatus.REJECTED, 'Request unsuccessful'),
    )

    user_book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey('auth.User')
    status = models.IntegerField(max_length=1, choices=_REQUEST_STATUS)
