from rest_framework import serializers
from payments.models import MakePayment
from .validation import Validate
from .models import Product


class PurchaseSerializer(serializers.ModelSerializer):
    validation = Validate()
    
    class Meta:
        model = MakePayment
        fields = "__all__"
        
        
    def validate(self, data):
        return_value = self.validation.validate(data)
        if type(return_value) is dict:
            raise serializers.ValidationError(return_value)
        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
    def validate(self, data):
        dictErrors = {}
        if not data['type'][0].isupper():
            dictErrors['type'] = 'The product name must start with a capital letter.'
        if data['price'] <= 0:
            dictErrors['price'] = 'The price cannot be negative or zero.'
        if data['availability'] < 0:
            dictErrors['availability'] = 'The availability cannot be negative'

        if len(dictErrors) > 0:
            raise serializers.ValidationError(dictErrors)
        return data