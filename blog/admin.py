from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ['title', 'active', 'author', 'image']
    ordering = ['-created_at']
    search_fields = ['title', 'body', 'author']
    summernote_fields = ('body',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['name', 'body']

admin.site.register(Comment,CommentAdmin)