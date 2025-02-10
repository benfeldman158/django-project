from django.contrib import admin
from .models import Product  # Import your model

admin.site.register(Product)  # Register the Product model to be managed via the admin panel
