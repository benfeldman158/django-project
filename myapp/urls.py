from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('help/', views.help_page, name='help'),  # Help page
]
