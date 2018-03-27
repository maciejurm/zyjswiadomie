from django import forms
from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        widgets = {
            'body': SummernoteWidget(attrs={'width': '100%', 'height': '400px'}),
        }
        