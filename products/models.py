from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#choices_product = (('book', 'book'), ('phone', 'phone'), ('whathces', 'whatches'), ('laptop', 'laptop'),
#                   ('freezer', 'freezer'), ('ball', 'ball'), ('TV', 'TV',), ('computer', 'computer'))

# Create your models here.


class Product(models.Model):
    type = models.CharField(db_index=True, max_length=20, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(99999.99)])
    availability = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.type
    
    def get_price(self):
        return self.price