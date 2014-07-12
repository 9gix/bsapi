from rest_framework import serializers
from transaction.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('book', 'borrow_membership', 'transaction_date', 'transaction_status')