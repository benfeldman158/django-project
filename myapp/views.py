from django.http import HttpResponse
from django.shortcuts import render

from .models import Product  # Import your Product model

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    results = Product.objects.filter(name__icontains=query)  # Search by name field
    return render(request, 'search.html', {'query': query, 'results': results})

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def help_page(request):
    return render(request, 'help.html')  # Make sure you have this template

