from django.db import models


class Conversation(models.Model):
    INITIALIZED = 'init'
    RESERVED = 'reserved'
    TRANSFERED = 'transfered'

    STATUS_CHOICES = (
        (INITIALIZED, 'Conversation Started'),
        (RESERVED, 'Book Reserved'),
        (TRANSFERED, 'Book Transfered'),
    )

    user_book = models.ForeignKey('ownership.UserBook')
    borrower = models.ForeignKey('auth.User')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=INITIALIZED)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation)
    content = models.TextField()

    sender = models.ForeignKey('auth.User', related_name='outbox_set')
    receiver = models.ForeignKey('auth.User', related_name='inbox_set')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

