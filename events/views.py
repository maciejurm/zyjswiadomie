from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def event_list(request):
    events = Event.objects.filter(active=True)
    paginator = Paginator(events, 9)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(num_pages)
    return render(request, 'list.html',
                 {'events': events,
                 'page': page})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 
                 'detail.html',
                 {'event': event})