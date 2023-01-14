from django.shortcuts import render

from article.models import *


def show_articles(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def new_article(request):
    return render(request, 'newArticle.html', {'form': ArticleCreationForm})


def add_new_article(request):
    if request.POST:
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data['title']
            article.text = form.cleaned_data['text']
            article.author = request.user
            article.save()
            return show_articles(request)
    else:
        form = ArticleCreationForm
    return render(request, 'newArticle.html', {'form': form})
