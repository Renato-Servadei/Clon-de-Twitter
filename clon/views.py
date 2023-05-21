from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Profile
from .forms import UserRegisterForm, PostForm, UserUpdateForm, ProfileUpdateForm

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

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    return render(request, 'twitter/profile.html', context={'user': user, 'posts': posts})

def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()  
    return render(request, 'twitter/editar.html', context={'u_form': u_form, 'p_form':p_form})