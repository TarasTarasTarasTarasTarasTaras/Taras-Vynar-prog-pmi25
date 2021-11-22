from django.contrib import admin
from .models import MakePayment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'currency', 'payer_email', 'request_date', 'transactionID', 'purchased')
    
admin.site.register(MakePayment, PaymentAdmin)