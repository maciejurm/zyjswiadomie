from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from meta.models import ModelMeta



def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(num_pages)
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

def nowy_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Post został dodany! Teraz czeka na akceptację przez moderatora. :)')
        else:
            messages.error(request, 'Błąd. Sprawdź czy zostały poprawnie wypełnione wszystkie pola.')
    else:
        form = PostForm()
    return render(request, 'blog/nowy.html', {'form': form})