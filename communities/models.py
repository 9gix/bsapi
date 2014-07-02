from django.db import models
from django.conf import settings

class Community(models.Model):
    name = models.CharField(max_length=40, unique=True)
    logo = models.ImageField(upload_to='community-logo', blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
            through='communities.Membership', related_name='communities')

    class Meta:
        verbose_name_plural = 'communities'

    def __str__(self):
        return self.name

class Membership(models.Model):
    community = models.ForeignKey('communities.Community')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    reputation = models.OneToOneField('reputation.Reputation')

    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {}".format(self.community, self.user)
