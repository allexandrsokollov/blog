from django.shortcuts import render

from article.models import Article


def show_articles(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def new_article(request):
    return render(request, 'newArticle.html')
