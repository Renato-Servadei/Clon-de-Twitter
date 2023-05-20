from django.shortcuts import render, redirect
from .models import Post, Profile
from .forms import UserRegisterForm, PostForm

def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else: 
        form = PostForm()
    return render(request, 'twitter/newsfeed.html', context={'posts': posts, 'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'twitter/register.html', context={'form': form})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')