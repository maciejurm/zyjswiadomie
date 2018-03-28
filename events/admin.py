from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

class EventAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'author']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
admin.site.register(Event, EventAdmin)
