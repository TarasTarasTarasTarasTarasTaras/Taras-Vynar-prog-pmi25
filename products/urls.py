from django.urls import path
from .views import *

urlpatterns = [
    path('', OrdersAPI.as_view()),
    path('<int:id>/', OrdersAPIwithID.as_view()),
    path('catalog/', ProductCatalogAPI.as_view()),
    path('addproduct/', ProductAPI.as_view())
]
