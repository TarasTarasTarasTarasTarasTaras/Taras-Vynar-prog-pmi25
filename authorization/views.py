#from rest_framework.views import APIView
from django.core import paginator
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import fields, serializers, status, filters, permissions
from .models import User
from .serializer import SignUpAPISerializer, SignInAPISerializer, LogOutSerializer

from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .documentations import DOCS

# Create your views here.



class SignUpAPI(generics.GenericAPIView):
    serializer_class = SignUpAPISerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body = DOCS.post_signup['body'],
        operation_description = DOCS.post_signup['operation_name'],
        responses = DOCS.post_signup['responses']
    )
    def post(self, request):
        serializerUser = self.serializer_class(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        serializerUser.save()
        
        return Response(serializerUser.data, status=status.HTTP_201_CREATED)
        
        
        
class SignInAPI(generics.GenericAPIView):
    serializer_class = SignInAPISerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body = DOCS.post_login['body'],
        operation_description = DOCS.post_login['operation_name'],
        responses = DOCS.post_login['responses']
    )
    def post(self, request):
        serializerUser = self.serializer_class(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        return Response(serializerUser.data, status=status.HTTP_200_OK)
        
        
class LogOutAPI(generics.GenericAPIView):
    serializer_class = LogOutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    @swagger_auto_schema(
        request_body = DOCS.post_logout['body'],
        operation_description = DOCS.post_logout['operation_name'],
        responses = DOCS.post_logout['responses']
    )
    def post(self, request):
        serializerUser = self.serializer_class(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        serializerUser.save()
        
        return Response({'status': '204',
                         'message': 'Logged out successfully'}, status=status.HTTP_204_NO_CONTENT,)