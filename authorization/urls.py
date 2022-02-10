from django.urls import path
from .views import *

urlpatterns = [
    path('login/', SignInAPI.as_view()),
    path('logout/', LogOutAPI.as_view()),
    path('users/', SignUpAPI.as_view()),
]