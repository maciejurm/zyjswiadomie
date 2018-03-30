from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

app_name = 'event'
urlpatterns = [
    path('wszystkie/', views.event_list, name='event_list'),
    path('wszystkie/dodaj/', views.nowe_wydarzenie, name='event_add'),
    path('<slug>/', views.event_detail, name='event_detail'),
]