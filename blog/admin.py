from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'author', 'image']
    ordering = ['-created_at']
    search_fields = ['title', 'body', 'author']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['name', 'body']

admin.site.register(Comment,CommentAdmin)