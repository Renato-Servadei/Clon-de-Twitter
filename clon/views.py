from django.shortcuts import render, redirect
from .models import Post, Profile
from .forms import UserRegisterForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'twitter/newsfeed.html', context={'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'twitter/register.html', context={'form': form})