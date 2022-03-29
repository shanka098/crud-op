from django.db import models

class supermarket(models.Model):
    productname = models.CharField(max_length=100)
    productid = models.IntegerField()
    price = models.IntegerField()
    Quantityinhand = models.IntegerField()
    soldquantity = models.IntegerField()
    Remainingstock = models.IntegerField()