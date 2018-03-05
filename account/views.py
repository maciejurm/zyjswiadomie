from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Follow, Profile
from blog.models import Post
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import FollowForm, LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


enricher = Enrich()

def follow(request):
    form = FollowForm(request.POST)
    if form.is_valid():
        follow = form.instance
        follow.user = request.user
        follow.save()

def unfollow(request, target_id):
    follow = Follow.objects.filter(user=request.user, target_id=target_id).first()
    if follow is not None:
        follow.delete()

def user(request, username):
    user = get_object_or_404(User, username=username)
    feeds = feed_manager.get_user_feed(user.id)
    activities = feeds.get()['results']
    activities = enricher.enrich_activities(activities)
    context = {   
        'user': user,
        'form': FollowForm(),
        'login_user': request.user,
        'activities': activities,
    }
    return render(request, 'profile/user.html', context)

@login_required
def timeline(request):
    enricher = Enrich()
    feed = feed_manager.get_news_feeds(request.user.id)
    activities = feed.get(limit=25)['results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'timeline.html', context)

def discover(request):
    users = User.objects.order_by('date_joined')[:50]
    login_user = User.objects.get(username=request.user)
    following = []
    for i in users:
        if len(i.followers.filter(user=login_user.id)) == 0:
            following.append((i, False))
        else:
            following.append((i, True))
    login_user = User.objects.get(username=request.user)
    context = {
        'users': users,
        'form': FollowForm(),
        'login_user': request.user,
        'following': following
    }
    return render(request, 'uzytkownicy.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane.')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'registration/register.html',
                 {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data = request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                'formularze/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})
        