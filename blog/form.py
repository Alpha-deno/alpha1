from django import forms
from .models import Blog,BlogComment,AnonyComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['message']

class AnonyCommentForm(forms.ModelForm):
    class Meta:
        model = AnonyComment
        fields = ['My_name', 'message']

