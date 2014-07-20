from django.contrib import admin
from conversation.models import Channel, ChannelMessage

admin.site.register(Channel)
admin.site.register(ChannelMessage)
