from rest_framework import viewsets

from reputation.models import Reputation
from reputation.serializers import ReputationSerializer

class ReputationViewSet(viewsets.ModelViewSet):
    model = Reputation
    serializer_class = ReputationSerializer
