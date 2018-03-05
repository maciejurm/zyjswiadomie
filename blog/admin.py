from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'author', 'image']
    ordering = ['-created_at']
    search_fields = ['title', 'body', 'author']

admin.site.register(Post, PostAdmin)
