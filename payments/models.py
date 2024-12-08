from django.db import models

# Create your models here.

class Payment(models.Model):
    payer_email = models.EmailField(max_length=100)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3)
    request_date = models.DateField()
    due_to_date = models.DateField()
    transactionID = models.CharField(max_length=11, unique=True)
