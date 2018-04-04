from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def nowe_wydarzenie(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            messages.success(request, 'Wydarzenie zostało dodane poprawnie. :) Pojawi się jak tylko zostanie zaakceptowane przez moderatora.')
        else:
            messages.error(request, 'Błąd. Sprawdź czy zostały wypełnione poprawnie wszystkie pola.')
    else:
        form = EventForm()
    return render(request, 'dodaj.html',
                 {'form': form})
