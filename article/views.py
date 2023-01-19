from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView

from article.models import *


def show_articles(request):
    articles = Article.objects.all()

    paginator = Paginator(articles, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'articles': articles, 'page_obj': page_obj})


def new_article(request):
    return render(request, 'newArticle.html', {'form': ArticleForm})


def add_new_article(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data['title']
            article.text = form.cleaned_data['text']
            article.author = request.user
            article.save()
            return show_articles(request)
    else:
        form = ArticleForm
    return render(request, 'newArticle.html', {'form': form})


class UpdateArticle(UpdateView):
    model = Article
    template_name = 'edit_article.html'
    context_object_name = 'article'
    fields = ['title', 'text']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        print(request.user)
        print(self.object.author)
        print(request.user == self.object.author)

        if request.user != self.object.author:
            return HttpResponseForbidden()

        return super().post(request, *args, **kwargs)


class DeleteArticle(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = '/'


class ArticleDetailView(DeleteView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
