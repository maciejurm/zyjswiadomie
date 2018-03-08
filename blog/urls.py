from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug>/', views.tresc_postu, name='tresc_postu'),
    path('post/nowy/', views.nowy_post, name='nowy'),
]