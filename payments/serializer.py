from rest_framework import serializers
from .validation import Validate
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    validation = Validate()
    
    class Meta:
        model = Payment
        fields = "__all__"
        
        
    def validate(self, data):
        return_value = self.validation.validate(data)
        if type(return_value) is dict:
            raise serializers.ValidationError(return_value)
        return data

