from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('help/', views.help_page, name='help'),  # Help page
    path('restricted/', views.restricted_page, name='restricted'),
    path('register/', views.register, name='register'),

     path('chat/', views.chat_room, name='chat_room'),
    path('chat/create/', views.create_message, name='create_message'),
    path('chat/update/<int:pk>/', views.update_message, name='update_message'),
    path('chat/delete/<int:pk>/', views.delete_message, name='delete_message'),
]
