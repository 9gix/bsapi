from rest_framework import serializers

from reputation.models import Reputation

class ReputationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reputation
