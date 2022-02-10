from django.db import models
from .validation import ValidateAmount, ValidateTransactionID
from products.models import Product
import random


_choices = (('usd', 'usd'), ('eur', 'eur'), ('uah', 'uah'))

# Create your models here.

class Payment(models.Model):
    payer_email = models.EmailField(max_length=100)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=_choices)
    request_date = models.DateField(auto_now_add=True)
    due_to_date = models.DateField()
    transactionID = models.CharField(max_length=11, unique=True)
    


class MakePayment(models.Model):
    purchased = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    payer_email = models.EmailField(max_length=100)
    currency = models.CharField(max_length=3, choices=_choices)
    amount = models.PositiveIntegerField(validators=[ValidateAmount(),])
    request_date = models.DateField(auto_now_add=True)
    due_to_date = models.DateField()
    transactionID = models.CharField(max_length=11, unique=True, validators=[ValidateTransactionID(),],)
    
    class Meta:
        verbose_name = "Зробити покупку"
        verbose_name_plural = "Зробити покупку"