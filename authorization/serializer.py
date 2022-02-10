import re
from rest_framework import serializers
from authorization.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class SignUpAPISerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=50,
        min_length=8,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'is_superuser', 'role']
        
        extra_kwargs = {
            "password": {"write_only": True, }
        }
        
    def create(self, validated_data):
        dictErrors = {}
        if not validated_data['first_name'].istitle():
            dictErrors['first_name'] = 'The name must begin with a capital letter'
        
        if not validated_data['last_name'].istitle():
            dictErrors['last_name'] = 'The name must begin with a capital letter'
        
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', validated_data['password']):
            dictErrors['password'] = 'Bad password format'
        
        if len(dictErrors) > 0:
            raise serializers.ValidationError(dictErrors)
        
        # manager method
        return User.objects.create_user(**validated_data)
        
        
        
        
class SignInAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'token', 'refresh']
        #read_only_fields = ['token']
        write_only_fields = ['password']

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        dictErrors = {}
        #if not re.fullmatch(r'[a-zA-Z0-9\.\-\_]{4,100}[@][a-z]{2,6}\.[a-z]{2,6}?', data['email']):
        #    dictErrors['email'] = 'Bad email format'
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', data['password']):
            dictErrors['password'] = 'Bad password format'

        if len(dictErrors) > 0:
            raise serializers.ValidationError(dictErrors)
        
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('The user with such email is not registered or incorrect password')
        
        return {
            'email' : user.email,
            'token' : user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }
        


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': ('Token is expired or invalid')    
    }
    
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
        