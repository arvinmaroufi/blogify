from django import forms
from .models import Category, Article


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'category', 'title', 'slug', 'body', 'image_banner', 'image_detail', 'active']
