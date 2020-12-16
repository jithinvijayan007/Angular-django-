from rest_framework import serializers
from test_app.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"