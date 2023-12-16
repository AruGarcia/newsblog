from django import forms
from newspaper.blog.models import Post


class YourPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'category', 'image']
