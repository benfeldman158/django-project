from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name (this will be searchable)
    description = models.TextField()  # A description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"