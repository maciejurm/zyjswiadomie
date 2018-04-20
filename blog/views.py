from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


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
    return render(request, 
                 'blog/detail.html',
                 {'post': post})

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