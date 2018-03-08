from django.conf.urls import include, url, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    # Logowanie i rejestracja
    path('logowanie/', auth_view.login, name='login'),
    path('logout/', auth_view.logout, name='logout'),
    path('logout-then-login/', auth_view.logout_then_login, name='logout_then_login'),
    path('password-change/', auth_view.password_change, name='password_change'),
    path('password-change/done/', auth_view.password_change_done, name='password_change_done'),
    path('password-reset/', auth_view.password_reset, name='password_reset'),
    path('password-reset/done/', auth_view.password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_view.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', auth_view.password_reset_complete, name='password_reset_confirm'),
    path('rejestracja/', views.register, name='registration'),
    path('edycja-profilu/', views.edit, name='edycja'),
    # Profil użytkownika
    path('users/', views.user_list, name='user_list'),
    path('profil/<username>/',
        views.user_detail,
        name='user_detail'),
]