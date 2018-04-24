from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.db.models import Count


def post_list(request, tag_slug=None):
    object_list = Post.objects.filter(active = True)
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(num_pages)
    return render(request, 
                 'blog/list.html',
                 {'posts': posts,
                 'tag': tag})

def tresc_postu(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-created_at')[:4]
    return render(request, 
                 'blog/detail.html',
                 {'post': post,
                 'similar_posts': similar_posts})

@login_required
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