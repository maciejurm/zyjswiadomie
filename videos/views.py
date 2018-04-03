from django.shortcuts import render, get_object_or_404
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/list.html',
                 {'videos': videos})

def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video/detail.html',
                 {'video': video})