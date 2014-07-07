from rest_framework import serializers
from transaction.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('book', 'borrower', 'transaction_date', 'transaction_status')