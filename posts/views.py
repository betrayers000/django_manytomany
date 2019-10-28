from django.shortcuts import render, redirect, get_object_or_404
from .forms import Postform
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = Postform()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)

def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    if post.like_users.filter(username=user.username):
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:index')