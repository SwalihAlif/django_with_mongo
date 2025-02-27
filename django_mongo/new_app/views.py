from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'index.html', {'posts': posts, 'form': form})