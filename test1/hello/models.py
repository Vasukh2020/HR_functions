from pickle import TRUE
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(blank=False)
    description =models.TextField(blank=TRUE)
    price = models.DecimalField( default=0, max_digits=1200, decimal_places=2)
    rating= models.DecimalField(max_digits=1, decimal_places=0, default=0)

