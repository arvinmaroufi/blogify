from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    image_banner = models.ImageField(upload_to='images/article/banner', blank=True, null=True)
    image_detail = models.ImageField(upload_to='images/article/detail', blank=True, null=True)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])
