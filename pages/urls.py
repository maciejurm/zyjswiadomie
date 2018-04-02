from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

urlpatterns = [
    path('kontakt/', views.KontaktView.as_view(), name='kontakt'),
    path('zostan-patronem/', views.PatronView.as_view(), name='patron'),
]    
    
