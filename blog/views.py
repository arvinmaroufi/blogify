from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import CreateCategory, CreateArticle
from django.core.paginator import Paginator
# Create your views here.


# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)


def articles_list(request):
    articles = Article.objects.filter(active=True)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': object_list})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    return render(request, 'blog/article_detail.html', {'article': article})


def search(request):
    search_article = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=search_article)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': object_list})


def category_create(request):
    if request.method == 'POST':
        forms = CreateCategory(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('blog:articles_list')
    else:
        forms = CreateCategory()
    return render(request, 'blog/category_create.html', {'forms': forms})


def article_create(request):
    if request.method == 'POST':
        forms = CreateArticle(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('blog:articles_list')
    else:
        forms = CreateArticle()
    return render(request, 'blog/article_create.html', {'forms': forms})


def article_update(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    forms = CreateArticle(request.POST or None, request.FILES or None, instance=articles)
    if forms.is_valid():
        forms.save()
        return redirect('blog:articles_list')
    return render(request, 'blog/article_update.html', {'articles': articles, 'forms': forms})


def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:articles_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})
