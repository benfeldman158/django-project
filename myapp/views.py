from django.http import HttpResponse
from django.shortcuts import render
from .models import Product  # Import your Product model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from .models import ChatMessage, Activity  # Import Activity model

@login_required
def activity_feed(request):
    activities = Activity.objects.all().order_by('-timestamp')[:20]  # Get the latest 20 activities
    return render(request, 'myapp/activity_feed.html', {'activities': activities})


def chat_room(request):
    messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'myapp/chat_room.html', {'messages': messages})
@login_required
def create_message(request):
    if request.method == "POST":
        message_text = request.POST.get('message', '')
        if message_text:
            ChatMessage.objects.create(user=request.user, message=message_text)
            Activity.objects.create(user=request.user, action="posted a message")
            return redirect('chat_room')
    return render(request, 'myapp/create_message.html')
@login_required
def update_message(request, pk):
    msg = get_object_or_404(ChatMessage, pk=pk, user=request.user)
    if request.method == "POST":
        new_message = request.POST.get('message', '')
        if new_message:
            msg.message = new_message
            msg.save()
            return redirect('chat_room')
    return render(request, 'myapp/update_message.html', {'message': msg})
@login_required
def delete_message(request, pk):
    msg = get_object_or_404(ChatMessage, pk=pk, user=request.user)
    if request.method == "POST":
        msg.delete()
        return redirect('chat_room')
    return render(request, 'myapp/delete_message.html', {'message': msg})

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
