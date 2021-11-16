from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaymentPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        offset = self.request.query_params.get('offset')
        limit = self.request.query_params.get('limit')

        return Response({
            'count': self.page.paginator.count, 
            'customers': data[int(offset)*int(limit):int(offset)*int(limit)+int(limit)] 
                if (offset and limit) is not None else data
        })
        