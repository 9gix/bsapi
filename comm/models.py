from django.db import models
from enum import Enum

class ReservationStatus:
    PENDING = 0
    ACCEPTED = 1
    REJECTED = -1


class Conversation(models.Model):
    STATUS_CHOICES = (
        (ReservationStatus.PENDING, 'Waiting for approval'),
        (ReservationStatus.ACCEPTED, 'Request approved'),
        (ReservationStatus.REJECTED, 'Request unsuccessful'),
    )

    user_book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey('auth.User')

    reservation_status = models.SmallIntegerField(
            choices=STATUS_CHOICES,
            default=ReservationStatus.PENDING)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation)
    content = models.TextField()

    sender = models.ForeignKey('auth.User', related_name='outbox_set')
    receiver = models.ForeignKey('auth.User', related_name='inbox_set')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

