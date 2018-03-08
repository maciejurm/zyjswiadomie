from django import forms
from .models import Comment, Post
from mediumeditor.widgets import MediumEditorTextarea


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        widgets = {
            'body': MediumEditorTextarea(),
        }
        