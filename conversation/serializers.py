from rest_framework import serializers

from conversation.models import (
        Channel, Message
)


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Message
        fields = ('channel', 'content', 'sender')

    def restore_object(self, attrs, instance=None):
        instance =super().restore_object(attrs, instance)
        instance.sender = self.context['request'].user
        return instance


class ChannelSerializer(serializers.ModelSerializer):
    message_set = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Channel
        fields = ('id', 'loan_request', 'appointment_at', 'message_set',)
