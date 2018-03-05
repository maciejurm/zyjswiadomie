from django.shortcuts import render, get_object_or_404
from .models import Post
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager


def post_list(request):
    posts = Post.objects.all()
    return render(request, 
                 'blog/list.html',
                 {'posts': posts})

def tresc_postu(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 
                 'blog/detail.html',
                 {'post': post})