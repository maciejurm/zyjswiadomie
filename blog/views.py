from django.shortcuts import render, get_object_or_404
from .models import Post
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 
                 'blog/list.html',
                 {'posts': posts})

def tresc_postu(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active = True)
    comment_form = CommentForm(data = request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 
                 'blog/detail.html',
                 {'post': post,
                 'comments': comments,
                 'comment_form': comment_form})