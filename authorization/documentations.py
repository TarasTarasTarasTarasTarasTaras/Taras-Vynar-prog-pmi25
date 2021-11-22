from drf_yasg import openapi
from .serializer import SignUpAPISerializer, SignInAPISerializer, LogOutSerializer

class DOCShelper:
    valid_user_example = {
        'email': 'name111@gmail.com',
        'token': 'eyJ0eXAiOiJKV1Q1NiJ9.eyJ0b2tlbl90eXBlwiZXhwIjoxNjM3...',
    }
    
    signup_valid = {
        "email": "ivan@gmail.com",
        "first_name": "Ivan",
        "last_name": "Petrenko"
    }
    
    signup_invalid = {
        "first_name": "The name must begin with a capital letter",
        "last_name": "The name must begin with a capital letter",
        "password": "Bad password format"
    }
    
    login_invalid = {
        'non_field_errors': 'The user with such email is not registered or incorrect password'
    }
    
    logout_valid = {
        "status": "204",
        "message": "Logged out successfully"
}

class DOCS:
    post_signup = {
        'operation_name': 'Creating a new user and storing in the database',
        'body': SignUpAPISerializer(),
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.signup_valid},
                                    description='The user has successfully created and saved to the database'),
            '400': openapi.Response(examples={'application/json': DOCShelper.signup_invalid},
                                    description='Error creating new user'),
        }
    }
    
    post_login = {
        'operation_name': 'User authorization in the system',
        'body': SignInAPISerializer(),
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.valid_user_example},
                                    description='The user has successfully logged in to the system'),
            '400': openapi.Response(examples={'application/json': DOCShelper.login_invalid},
                                    description='The user with such email is not registered or incorrect password')
        }
    }
    
    post_logout = {
        'operation_name': 'The user logs off',
        'body': LogOutSerializer(),
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.logout_valid},
                                    description='The user has successfully logged out'),
            '400': openapi.Response(description='Token is expired or invalid')
        }
    }