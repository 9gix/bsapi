from django.db import models

class Channel(models.Model):
    user_book_request = models.OneToOneField('reservation.UserBookRequest')
    appointment_at = models.DateTimeField(blank=True, null=True)


class ChannelMessage(models.Model):
    channel = models.ForeignKey(Channel)
    content = models.TextField()

    sender = models.ForeignKey('auth.User', related_name='outbox_set')
    receiver = models.ForeignKey('auth.User', related_name='inbox_set')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

