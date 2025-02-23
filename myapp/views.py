from django.http import HttpResponse
from django.shortcuts import render
from .models import Product  # Import your Product model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    results = Product.objects.filter(name__icontains=query) if query else []  # Search by name field
    return render(request, 'myapp/search.html', {'query': query, 'results': results})

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def help_page(request):
    return render(request, 'myapp/help.html')  # Updated path for consistency

@login_required
def restricted_page(request):
    return render(request, 'myapp/restricted.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in after registration
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})
