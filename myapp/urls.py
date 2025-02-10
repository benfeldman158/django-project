from django.urls import path
from . import views  # Import views from your app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('help/', views.help_page, name='help'),  # Help page
]
