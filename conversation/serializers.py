from rest_framework import serializers

from conversation.models import (
        Channel, Message
)


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='username', read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='message-detail',
            lookup_field='pk')
    class Meta:
        model = Message
        fields = ('url', 'channel', 'content', 'sender')

    def restore_object(self, attrs, instance=None):
        instance =super().restore_object(attrs, instance)
        instance.sender = self.context['request'].user
        return instance


class ChannelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='channel-detail',
            lookup_field='pk')
    message_set = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Channel
        fields = ('id', 'url', 'loan_request', 'appointment_at', 'message_set',)
