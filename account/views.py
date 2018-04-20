from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Profile, Follow
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from common.decorators import ajax_required
from django.views.decorators.http import require_POST


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
            profile = Profile.objects.create(user=new_user)
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

def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'uzytkownicy.html',
                {'section': 'people',
                'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'profile/user.html',
                  {'section': 'people',
                   'user': user})
@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id', None)
    action = request.POST.get('action', '')

    FOLLOW_ACTION = 'follow'
    UNFOLLOW_ACTION = 'unfollow'

    if request.user.is_anonymous:
        return JsonResponse({
            'status':'ko',
            'message': 'You must login'}
        )

    if action not in [FOLLOW_ACTION, UNFOLLOW_ACTION]:
        return JsonResponse({
            'status':'ko',
            'message': 'Unknown action {}'.format(action)}
        )

    try:
        user = User.objects.get(id=user_id)
        if action == UNFOLLOW_ACTION:
            Follow.objects.filter(user=request.user,target=user).delete()
            return JsonResponse({
                'status':'ok'
                })
        else:
            contact, created = Follow.objects.get_or_create( user=request.user, target=user)
            return JsonResponse({
                'status':'ok',
                'message': 'Following id : {}'.format(follow.id)
            })


    except User.DoesNotExist:
        return JsonResponse({
            'status':'ko'
        })