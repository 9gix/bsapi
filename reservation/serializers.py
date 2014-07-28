from rest_framework import serializers

from reservation.models import LoanRequest
from communities.models import Membership

class LoanRequestSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="loanrequest-detail",
            lookup_field='pk')
    status = serializers.CharField(source='status', read_only=True)

    class Meta:
        model = LoanRequest
        fields = ('url', 'id', 'owner_book', 'borrower_membership', 'status',
                'channel', 'transaction')

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        # limit membership choices to the current user
        user = self.context['view'].request.user
        qs = fields['borrower_membership'].queryset
        fields['borrower_membership'].queryset = qs.filter(user=user)

        return fields
