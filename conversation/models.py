from django.db import models

class Channel(models.Model):
    loan_request = models.OneToOneField('reservation.LoanRequest')
    appointment_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.loan_request)


class ChannelMessage(models.Model):
    channel = models.ForeignKey(Channel)
    content = models.TextField()

    sender = models.ForeignKey('auth.User', related_name='outbox_set')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "[{}] {}: {}".format(self.channel, self.sender, self.content)
