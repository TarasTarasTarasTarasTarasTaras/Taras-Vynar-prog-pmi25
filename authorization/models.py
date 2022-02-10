from django.db import models

import jwt
from jwt import PyJWT

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

from enum import Enum
from .validation import ValidateFirstLastName, ValidatePassword
# Create your models here.



class Roles(Enum):
    user = 0
    admin = 1

    @classmethod
    def items(cls):
        return [(option.value, option.name) for option in cls]



class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, validators=[ValidateFirstLastName('first_name'),])
    last_name = models.CharField(max_length=50, validators=[ValidateFirstLastName('last_name'),])
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255, validators=[ValidatePassword(),])
    role = models.IntegerField(choices=Roles.items(), default=0)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password',]
    objects = UserManager()
    
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        #return str(refresh.access_token)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
    
