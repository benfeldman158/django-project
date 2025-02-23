from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help'),
    path('restricted/', views.restricted_page, name='restricted'),
]
