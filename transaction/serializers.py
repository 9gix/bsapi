from django.db.models import Q

from rest_framework import serializers

from transaction.models import Transaction
from reservation.models import LoanRequest

class TransactionSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
            view_name="transaction-detail",
            lookup_field='pk')

    class Meta:
        model = Transaction
        fields = ('url', 'loan_request', 'transaction_date')

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        user = self.context['view'].request.user
        if self.object:
            qs = Q(transaction__isnull=True)|Q(pk=self.object.loan_request.pk)
        else:
            qs = Q(transaction__isnull=True)
        loanrequests = LoanRequest.objects.filter(qs, owner_book__owner=user)
        fields['loan_request'].queryset = loanrequests
        return fields
