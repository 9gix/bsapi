from rest_framework import serializers

from conversation.models import (
        Channel, Message
)

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('channel', 'content', 'sender')
        read_only_fields = ('sender',)

    def restore_object(self, attrs, instance=None):
        instance =super().restore_object(attrs, instance)
        instance.sender = self.context['request'].user
        return instance
