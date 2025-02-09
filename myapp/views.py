from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse("This is the About Page!")

def help_page(request):
    return render(request, 'help.html')  # Make sure you have this template
