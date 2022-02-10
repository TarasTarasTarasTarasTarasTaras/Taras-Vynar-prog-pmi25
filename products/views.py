from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, filters, permissions

from .models import Product
from .serializer import PurchaseSerializer, ProductSerializer
from .validation import exchange_rate
from .documentations import DOCSOrder, DOCSProduct

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from payments.pagination import ClassPagination
from payments.models import MakePayment
from payments.serializer import PaymentSerializer


# Create your views here.


# каталог (список доступних продуктів для замовлення) localhost:8000/orders/catalog/
# доступно неавторизованим користувачам
@method_decorator(
    name="get",
    decorator=swagger_auto_schema(**DOCSProduct.get)
)
class ProductCatalogAPI(ListAPIView):
    pagination_class = ClassPagination
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ('id', 'type', 'price', 'availability')
    serializer_class = ProductSerializer



class OrdersAPI(ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]

    # отримуємо список замовлень авторизованого користувача
    @swagger_auto_schema(**DOCSOrder.get)
    def get(self, request):
        payments = MakePayment.objects.filter(payer_email=request.user.email).values()
        return Response({"status": 200,
                         "number of orders": len(payments),
                         "orders": payments},
                         status=status.HTTP_200_OK)


    # замовляємо продукт (робимо платіж). список доступних продуктів для замовлення в бд Product
    @swagger_auto_schema(**DOCSOrder.post)
    def post(self, request):
        serializerOrder = PurchaseSerializer(data=request.data)
        if serializerOrder.is_valid():
            serializerOrder.save()
            pr = Product.objects.get(pk=request.data['purchased'])
            pr.availability = pr.availability - 1
            pr.save()
            return Response({"status": 200,
                             "message": "You have successfully purchased the "+str(pr)+", " +str(pr)+"s left in stock: " +str(pr.availability) +
                             ". Your rest: " +str(request.data['amount']/exchange_rate[request.data['currency']] - pr.price)+
                             " usd. Thanks for buying :)",
                             "payment": serializerOrder.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializerOrder.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class OrdersAPIwithID(ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get_object_or_response(self, request, id):
        try:
            order = MakePayment.objects.filter(payer_email = request.user.email)
            return order[id-1]
        except:
            return Response({'status' : '404',
                             'message' : f'Order with id = {id} for this user not found', },
                            status = status.HTTP_404_NOT_FOUND)


    # отримуємо замовлення авторизованого користувача за ідентифікатором
    @swagger_auto_schema(**DOCSOrder.get_id)
    def get(self, request, id):
        order = self.get_object_or_response(request, id)
        if type(order) is Response:
            return order
        serializerOrder = PaymentSerializer(order)
        return Response(serializerOrder.data)
    
    
    
class ProductAPI(ListAPIView):
    permission_classes = [permissions.IsAdminUser,]
    
    # додаємо продукт до бд Product (лише адмін) localhost:8000/orders/addproduct/
    @swagger_auto_schema(**DOCSProduct.post)
    def post(self, request):
        serializerProduct = ProductSerializer(data=request.data)
        if serializerProduct.is_valid():
            serializerProduct.save()
            return Response({"status": 200,
                             "message": "You have successfully added the product to the database",
                             "product": serializerProduct.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializerProduct.errors, status=status.HTTP_400_BAD_REQUEST)