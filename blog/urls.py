from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('detail/<slug:slug>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search_articles'),
    path('category_create/', views.category_create, name='category_create'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_update/<slug:slug>/', views.article_update, name='article_update'),
    path('article_confirm_delete/<slug:slug>/', views.article_delete, name='article_delete'),
]
