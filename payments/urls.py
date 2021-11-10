from django.urls import path
from .views import *

urlpatterns = [
    path('', PaymentAPI.as_view()),
    path('<int:id>/', PaymentAPIwithID.as_view()), 
]
