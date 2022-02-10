from copy import error
import re
from rest_framework import serializers
from django.db import models
from datetime import date
from products.validation import exchange_rate

class ValidateAmount:
    def __call__(self, value):
        if value > 999999:
            raise serializers.ValidationError({'amount': 'Amount must be no less than 0 and no more than 999999'})


class ValidateTransactionID:
    def __call__(self, value):
        if not re.fullmatch(r'\d{8}-\d{2}', value): # ********-** only numbers
            raise serializers.ValidationError({'transactionID': 'TransactionID must be in the format: ********-** and contains only numbers'})
            
            
class ValidateTwoDates:
    def __init__(self, request_date):
        self.request_date = request_date
        
    def __call__(self, value):
        if value > self.request_date:
            raise serializers.ValidationError({'request_date': 'Request date must be < Due to date'})

            
class Validate:
    dictErrors = {}
    
    def validate(self, data):
        self.__validate_amount(data['amount'])
        self.__validate_currency(data['currency'])
        self.__validate_transactionID(data['transactionID'])
        self.__validate_twoDates(data['request_date'], data['due_to_date'])
        if len(self.dictErrors) > 0:
            return self.dictErrors
        
        
    def __validate_twoDates(self, value1, value2):
        if value1 > value2:
            self.dictErrors['request_date'] = 'Request date must be < Due to date'
        
        
    def __validate_amount(self, value):
        if value > 999999:
            self.dictErrors['amount'] = 'Amount must be no less than 0 and no more than 999999'
        

    def __validate_currency(self, value):
        if value != "usd" and value != "eur" and value != "uah":
            self.dictErrors['currency'] = 'Currency must be only usd/eur/uah'
    
    
    def __validate_transactionID(self, value):
        if not re.fullmatch(r'\d{8}-\d{2}', value): # ********-** only numbers
            self.dictErrors['transactionID'] = 'TransactionID must be in the format: ********-** and contains only numbers'
            