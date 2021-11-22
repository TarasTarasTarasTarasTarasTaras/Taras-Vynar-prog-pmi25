import re
from rest_framework import serializers

class ValidateFirstLastName:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __call__(self, value):
        if not value.istitle():
            raise serializers.ValidationError({self.attribute: 'The name must begin with a capital letter'})
        
        
class ValidatePassword:
    def __call__(self, value):
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', value):
             raise serializers.ValidationError({'password': 'Bad password format'})