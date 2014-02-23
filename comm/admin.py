from django.contrib import admin
from comm.models import Conversation, ConversationMessage

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
