from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

app_name = 'film'
urlpatterns = [
    path('wszystkie/', views.video_list, name='video_list'),
    path('<slug>/', views.video_detail, name='video_detail'),
    path('video/dodaj/', views.video_add, name='video_add'),
]