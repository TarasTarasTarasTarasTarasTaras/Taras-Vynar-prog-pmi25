from rest_framework import serializers

from .models import Product
from authorization.models import User

exchange_rate = {'uah': 27, 'eur': 0.89, 'usd': 1} # курс валюти відносно долара

class Validate:
    dictErrors = {}
    
    def validate(self, data):
        #product = Product.objects.get(pk=data['purchased'].id)
        product = data['purchased']
        self.__find_email_in_the_database(data['payer_email'])
        self.__check_the_availability(data, product)
        self.__check_the_specified_amount(data, product)
        if len(self.dictErrors) > 0:
            return self.dictErrors
        
        
    def __find_email_in_the_database(self, email_):
        try:
            User.objects.get(email=email_)
        except:
            self.dictErrors['email'] = 'The user with such email is not registered'
        
        
    def __check_the_availability(self, data, product):
        if product.availability == 0:
            self.dictErrors['availability'] = 'Sorry, but the product is over. Please try again later'
        
            
    def __check_the_specified_amount(self, data, product):
        if product.price > data['amount'] / exchange_rate[data['currency']]:
            self.dictErrors['amount'] = 'You have specified an insufficient amount'
    

class ValidateType:
    def __call__(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError({'type': 'The product name must start with a capital letter.'})