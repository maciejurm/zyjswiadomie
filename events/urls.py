from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

app_name = 'event'
urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<slug>/', views.event_detail, name='event_detail'),
]