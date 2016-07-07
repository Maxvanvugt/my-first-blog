from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    all_posts = Post.objects.all()
    return render(request,'blog/index.html', {'all_posts': all_posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
