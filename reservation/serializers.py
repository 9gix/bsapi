from rest_framework import serializers

from reservation.models import LoanRequest
from communities.models import Membership

class LoanRequestSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name="loanrequest-detail",
            lookup_field='pk')
    status = serializers.CharField(
            source='status',
            read_only=True)
    book_title = serializers.CharField(
            source='owner_book.book.title',
            read_only=True)
    book_isbn = serializers.CharField(
            source='owner_book.book.isbn13',
            read_only=True)
    owner_username = serializers.CharField(
            source='owner_book.owner.username',
            read_only=True)
    owner_fullname = serializers.CharField(
            source='owner_book.owner.get_full_name',
            read_only=True)
    borrower_username = serializers.CharField(
            source='borrower_membership.user.username',
            read_only=True)
    borrower_fullname = serializers.CharField(
            source='borrower_membership.user.get_full_name',
            read_only=True)
    community = serializers.CharField(
            source='borrower_membership.community.name',
            read_only=True)
    is_my_book = serializers.SerializerMethodField(
            'is_mine')

    class Meta:
        model = LoanRequest
        fields = ('url', 'id', 'owner_book', 'borrower_membership', 'status',
                'channel', 'transaction', 'book_title', 'owner_username',
                'owner_fullname', 'book_isbn', 'borrower_username',
                'borrower_fullname', 'community', 'is_my_book')
        read_only_fields = ('channel', 'transaction')

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        # limit membership choices to the current user
        user = self.context['view'].request.user
        qs = fields['borrower_membership'].queryset
        fields['borrower_membership'].queryset = qs.filter(user=user)

        return fields

    def is_mine(self, obj):
        return obj.owner_book.owner == self.context['request'].user
