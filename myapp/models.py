from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name (this will be searchable)
    description = models.TextField()  # A description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price

    def __str__(self):
        return self.name
