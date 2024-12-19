from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'created', 'active']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['title']
