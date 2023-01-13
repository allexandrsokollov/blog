from django.shortcuts import render
from .models import Article


def mian_page(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})
