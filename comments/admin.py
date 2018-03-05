from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('active', 'created_at', 'body')
    search_fields = ('name', 'body')

admin.site.register(Comment, CommentAdmin)
