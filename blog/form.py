from django import forms
from .models import Blog,BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['message']

