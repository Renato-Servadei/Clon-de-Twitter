from django.shortcuts import render
from .models import Post, Profile

def home(request):
    posts = Post.objects.all()
    return render(request, 'twitter/newsfeed.html', context={'posts': posts})
