#from rest_framework.views import APIView
from django.core import paginator
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import status, filters
from .models import Payment
from .serializer import PaymentSerializer

from drf_yasg.utils import swagger_auto_schema
from .documentations import DOCS
from django.utils.decorators import method_decorator
from .pagination import PaymentPagination



# Create your views here.
@method_decorator(
    name="get",
    decorator=swagger_auto_schema(operation_description = DOCS.get['operation_name'],
                                  responses = DOCS.get['responses'])
)
class PaymentAPI(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    #pagination_class = PaymentPagination    
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ('id', 'payer_email', 'amount', 'currency', 'request_date', 'due_to_date', 'transactionID')
    
    
    '''
    @swagger_auto_schema(
        operation_description = DOCS.get['operation_name'],
        responses = DOCS.get['responses']
    )
    def get(self, request):
        payments = Payment.objects.all()
        serializerPayment = PaymentSerializer(payments, many=True)        
        return Response(serializerPayment.data)
    '''
    
    
    @swagger_auto_schema(
        request_body = DOCS.post['body'],
        operation_description = DOCS.post['operation_name'],
        responses = DOCS.post['responses']
    )
    def post(self, request):
        serializerPayment = PaymentSerializer(data=request.data)
        if serializerPayment.is_valid():
            serializerPayment.save()
            return Response({"status": 200, 
                             "message": "Payment has been successfully created.",
                             "payment": serializerPayment.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializerPayment.errors, status=status.HTTP_400_BAD_REQUEST)



class PaymentAPIwithID(ListAPIView):
    def get_object_or_response(self, id):
        try:
            return Payment.objects.get(pk = id)
        except Payment.DoesNotExist:
            return Response({'status' : '404',
                             'message' : f'Payment with id = {id} not found', },
                            status = status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description = DOCS.getId['operation_name'],
        responses = DOCS.getId['responses']
    )
    def get(self, request, id):
        payment = self.get_object_or_response(id)
        if type(payment) is Response:
            return payment
        serializerPayment = PaymentSerializer(payment)
        return Response(serializerPayment.data)
    
    @swagger_auto_schema(
        request_body = DOCS.put['body'],
        operation_description = DOCS.put['operation_name'],
        responses = DOCS.put['responses']
    )
    def put(self, request, id):
        payment = self.get_object_or_response(id)
        if type(payment) is Response:
            return payment
        
        serializerPayment = PaymentSerializer(payment, data=request.data)
        if serializerPayment.is_valid():
            serializerPayment.save()
            return Response({"status": 200, 
                             "message": f"Payment with id = {id} has been successfully updated.",
                             "payment": serializerPayment.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializerPayment.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_description = DOCS.delete['operation_name'],
        responses = DOCS.delete['responses']
    )
    def delete(self, request, id):
        payment = self.get_object_or_response(id)
        if type(payment) is Response:
            return payment
        
        payment.delete()
        return Response({"status": 200,
                         "message": f"Payment with id = {id} was successfully deleted"},
                        status=status.HTTP_200_OK)

