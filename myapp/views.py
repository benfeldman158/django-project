from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def help_page(request):
    return render(request, 'help.html')  # Make sure you have this template

