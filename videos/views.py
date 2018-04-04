from django.shortcuts import render, get_object_or_404
from .models import Video
from django.contrib.auth.decorators import login_required
from .forms import VideoForm
from django.contrib import messages

def video_list(request):
    videos = Video.objects.filter(active=True)
    return render(request, 'video/list.html',
                 {'videos': videos})

def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video/detail.html',
                 {'video': video})

@login_required
def video_add(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            messages.success(request, 'Film został dodany poprawnie, zostanie wyświetlony po akceptacji moderatora. :)')
        else:
            messages.error(request, 'Błąd! Sprawdź czy poprawnie wypełniłeś wszystkie pola.')
    else:
        form = VideoForm()
    return render(request, 'video/dodaj.html',
                            {'form': form})