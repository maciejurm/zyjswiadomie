from django.contrib import admin
from .models import Post, Comment
from mediumeditor.admin import MediumEditorAdmin

class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    list_display = ['title', 'active', 'author', 'image']
    ordering = ['-created_at']
    search_fields = ['title', 'body', 'author']
    mediumeditor_fields = ('body', )

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['name', 'body']

admin.site.register(Comment,CommentAdmin)